# AE2 & Addons Texture Backport

Release **1.2.3**: Lightning Tech pattern provider GUI fixes. See the [release notes](docs/releases/1.2.3.md).

**English** | [简体中文](README.zh-CN.md)

Backported AE2 and addon textures and interfaces for **Minecraft 1.20.1 / Forge**.

This repository contains the editable merged resource pack. Interfaces mainly come from AE-Light-UI; quantum computer world textures and effects incorporate AE2LightMode, with selected newer item textures, models and compatibility fixes. This is not a complete backport of every newer resource. See the version-specific audit reports for differences.

## Installation

1. Download the ZIP from [v1.2.3](https://github.com/yxchen-leo/AE2-Addons-Texture-Backport/releases/tag/v1.2.3), place it in `resourcepacks` and enable it.
2. Install **AE2 Light UI Compat 1.2.3** in `mods`.
3. Remove the previous JAR, disable older merged packs and both source packs, and restart the client.

Since v1.2.1, installed mods supply their own GuideME pages. v1.2.2 adds only two targeted ExpandedAE page corrections. The optional mekmm loot fix is in the companion JAR; this ZIP alone does not change server loot. Single-player uses the client installation. Install the JAR on dedicated servers to enable that loot fix there.

## Repository contents

- `pack/`: editable resource pack, including credits and licenses.
- `CREDITS.txt`: sources and change history; the old companion namespace became `ae2lightuicompat` in 1.0.3.
- `file-provenance.json`: per-file sources and SHA-256 hashes.
- `sources/`: source and change manifests, without complete third-party mod JARs.
- `docs/` and `audit/`: release notes and reports. Historical reports apply to their stated versions.
- `package.py`: run `python package.py` to create the ZIP in `dist/`.

See the [1.1.2 support audit](docs/1.1.2-完整核对.md) and [1.2.1 static report](audit/1.2.1/validation.json). Compilation and static checks do not constitute in-game visual acceptance; each release documents its scope.

## Licensing and distribution

This repository remains private. **Public redistribution permissions for all third-party assets have not been fully verified.** AE2LightMode-1.20.1-V1.0.6 did not include an explicit permission statement; other sources also require per-file review. See the [license review](docs/许可核对.md).

Assets retain their original licenses. The companion mod's MIT license does not cover this pack. Attribution and private hosting do not establish redistribution permission. This unofficial backport does not imply endorsement by AE2 or addon authors.
