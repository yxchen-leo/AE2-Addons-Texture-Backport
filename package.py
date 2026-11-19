"""Validate and package the resource tree using only the Python standard library."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import tempfile
import zipfile
import zlib

ROOT = Path(__file__).resolve().parent
NAME = "AE2-Addons-Texture-Backport-1.20.1-v1.2.8.zip"
ZIP_TIMESTAMP = (2026, 10, 15, 0, 0, 0)
RESOURCE_PATH = re.compile(r"assets/[a-z0-9_.-]+/[a-z0-9/._-]+\Z")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(data):
    return json.loads(data, object_pairs_hook=unique_object)


def check_png(data):
    """Check PNG chunks and compressed image data without rewriting the image."""
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("Invalid PNG signature")
    offset = 8
    compressed = []
    while offset + 12 <= len(data):
        size = struct.unpack_from(">I", data, offset)[0]
        kind = data[offset + 4:offset + 8]
        end = offset + 12 + size
        if end > len(data):
            raise ValueError("Truncated PNG chunk")
        chunk = data[offset + 8:end - 4]
        crc = struct.unpack_from(">I", data, end - 4)[0]
        if zlib.crc32(kind + chunk) != crc:
            raise ValueError("PNG chunk checksum mismatch")
        if offset == 8:
            if kind != b"IHDR" or size != 13:
                raise ValueError("Missing PNG header")
            width, height = struct.unpack_from(">II", chunk)
            if not width or not height:
                raise ValueError("Empty PNG image")
        if kind == b"IDAT":
            compressed.append(chunk)
        if kind == b"IEND":
            if size or not compressed:
                raise ValueError("Incomplete PNG image")
            zlib.decompress(b"".join(compressed))
            # Some upstream files contain redundant bytes after IEND. Preserve them.
            return len(data) - end
        offset = end
    raise ValueError("Missing PNG end chunk")


def validate(source):
    provenance = read_json((ROOT / "file-provenance.json").read_bytes())
    files = {}
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Resource tree contains a symbolic link: {path}")
        if path.is_file():
            files[path.relative_to(source).as_posix()] = path
    if files.keys() != provenance.keys():
        missing = sorted(provenance.keys() - files.keys())
        unrecorded = sorted(files.keys() - provenance.keys())
        raise ValueError(f"Provenance mismatch; missing={missing}, unrecorded={unrecorded}")
    metadata = read_json((source / "pack.mcmeta").read_bytes())
    if metadata["pack"]["pack_format"] != 15:
        raise ValueError("Expected Minecraft 1.20.1 pack_format 15")
    json_count = png_count = 0
    validated = {}
    for name, path in files.items():
        if name.startswith("assets/") and not RESOURCE_PATH.fullmatch(name):
            raise ValueError(f"Invalid resource path: {name}")
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != provenance[name]["sha256"]:
            raise ValueError(f"Provenance checksum mismatch: {name}")
        try:
            if path.suffix in (".json", ".mcmeta"):
                read_json(data)
                json_count += 1
            elif path.suffix == ".png":
                trailing = check_png(data)
                if trailing:
                    print(f"Notice: {name} retains {trailing} upstream bytes after PNG IEND")
                png_count += 1
        except (ValueError, struct.error, zlib.error) as error:
            raise ValueError(f"{name}: {error}") from error
        validated[name] = data
    print(f"Validated {len(files)} files: {json_count} JSON/metadata, {png_count} PNGs")
    return validated


def package(files, target):
    target = target.resolve()
    source = (ROOT / "pack").resolve()
    if target == source or source in target.parents:
        raise ValueError("Output must be outside the pack/ resource tree")
    target.parent.mkdir(parents=True, exist_ok=True)
    # Replace the destination only after the complete temporary ZIP has passed CRC checks.
    with tempfile.NamedTemporaryFile(dir=target.parent, suffix=".tmp", delete=False) as temporary:
        temporary_path = Path(temporary.name)
    try:
        with zipfile.ZipFile(temporary_path, "w", zipfile.ZIP_DEFLATED) as archive:
            for name, data in files.items():
                info = zipfile.ZipInfo(name, ZIP_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, data)
        with zipfile.ZipFile(temporary_path) as archive:
            corrupt = archive.testzip()
            if corrupt is not None:
                raise ValueError(f"ZIP checksum mismatch: {corrupt}")
        temporary_path.replace(target)
    finally:
        temporary_path.unlink(missing_ok=True)
    print(target)
    print("SHA-256:", hashlib.sha256(target.read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Validate without writing a ZIP")
    mode.add_argument("--output", type=Path, help="Write a verification ZIP at a custom path")
    args = parser.parse_args()
    try:
        files = validate(ROOT / "pack")
        if not args.check:
            package(files, args.output or ROOT / "dist" / NAME)
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Packaging failed: {error}\n")


if __name__ == "__main__":
    main()
