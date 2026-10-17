"""Package the checked-in resource tree; Python standard library only."""
from pathlib import Path
import zipfile
import hashlib

ROOT = Path(__file__).resolve().parent
NAME = "AE2-Addons-Texture-Backport-1.20.1-v1.0.3.zip"

def main():
    source = ROOT / "pack"
    assert (source / "pack.mcmeta").is_file()
    target = ROOT / "dist" / NAME
    target.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                info = zipfile.ZipInfo(path.relative_to(source).as_posix(), (2026, 10, 15, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
    print(target.name)
    print("SHA-256:", hashlib.sha256(target.read_bytes()).hexdigest())

if __name__ == "__main__":
    main()
