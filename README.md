# AE2 & Addons Texture Backport

Release **1.2.7**: author `cyx` and a fixed resource pack display name. See the [release notes](docs/releases/1.2.7.md).

**English** | [简体中文](README.zh-CN.md)

Backported AE2 and addon textures and interfaces for **Minecraft 1.20.1 / Forge**.

This repository contains the editable merged resource pack. Interfaces mainly come from AE-Light-UI; quantum computer world textures and effects incorporate AE2LightMode, with selected newer item textures, models and compatibility fixes. This is not a complete backport of every newer resource. See the version-specific audit reports for differences.

## Installation

1. Download the ZIP from [v1.2.7](https://github.com/yxchen-leo/AE2-Addons-Texture-Backport/releases/tag/v1.2.7), place it in `resourcepacks` and enable it.
2. Install **AE2 Light UI Compat 1.2.7** in `mods`.
3. Remove the previous JAR, disable older merged packs and both source packs, and restart the client.

Since v1.2.1, installed mods supply their own GuideME pages. v1.2.2 adds only two targeted ExpandedAE page corrections. The optional mekmm loot fix is in the companion JAR; this ZIP alone does not change server loot. Single-player uses the client installation. Install the JAR on dedicated servers to enable that loot fix there.

## Repository contents

- `pack/`: editable resource pack, including credits and licenses.
- [pack/CREDITS.txt](pack/CREDITS.txt): canonical sources and change history; the old companion namespace became `ae2lightuicompat` in 1.0.3.
- `file-provenance.json`: per-file sources and SHA-256 hashes.
- `sources/`: source and change manifests, without complete third-party mod JARs.
- `docs/`: [documentation index](docs/README.md), release notes and reports. Machine-readable historical reports are grouped by version in `docs/verification/`.
- `package.py`: run `python package.py` with Python 3 to create the ZIP in `dist/`; no third-party Python packages are needed.

Only `pack/` is included in the ZIP. `dist/`, logs and editor caches are local outputs and are not tracked. Keep the current release ZIP locally; older builds can be downloaded from GitHub Releases. The root `CREDITS.txt` points to the complete attribution bundled in the pack.

See the [1.1.2 support audit](docs/1.1.2-完整核对.md) and [1.2.1 static report](docs/verification/1.2.1/validation.json). Compilation and static checks do not constitute in-game visual acceptance; each release documents its scope.

## Licensing and distribution

**Public redistribution permissions for all third-party assets have not been fully verified.** AE2LightMode-1.20.1-V1.0.6 did not include an explicit permission statement; other sources also require per-file review. See the [license review](docs/许可核对.md).

Assets retain their original licenses. The companion mod's MIT license does not cover this pack. Attribution and private hosting do not establish redistribution permission. This unofficial backport does not imply endorsement by AE2 or addon authors.
