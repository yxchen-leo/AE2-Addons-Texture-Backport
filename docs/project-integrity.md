# Project integrity / 项目完整性

Review date / 核对日期：2026-11-19。

## Files and packaging / 文件与打包

- 4,467 retained files match the current provenance inventory and SHA-256 values. All 2,495 JSON/metadata files parse without duplicate keys. All 1,965 PNGs pass signature, chunk CRC and compressed-data checks.
- 保留的 4,467 个文件与当前来源清单及 SHA-256 一致；2,495 份 JSON/元数据均可解析且无重复键；1,965 张 PNG 通过签名、数据块 CRC 及压缩数据检查。
- Removed only `pack/assets/ae2/lang/zh_cn.etag`, an unreferenced download-cache token, and its current provenance entry. Historical source manifests remain unchanged. Retained visual resources are unchanged, including the source GIF and licenses; pack metadata is updated to v1.2.8.
- 仅删除无引用的下载缓存 `pack/assets/ae2/lang/zh_cn.etag` 及当前来源清单对应项；历史来源清单保留原样。保留的视觉资源字节不变，包括原始 GIF 和许可证；资源包元数据更新为 v1.2.8。
- `ex_emc_import_bus.png` has 26 redundant bytes after a valid PNG IEND. Its chunk CRCs and compressed data are valid; the original bytes are preserved and the checker reports a notice.
- `ex_emc_import_bus.png` 在有效 PNG 结束块后含 26 字节冗余尾部。块校验和及压缩数据正常，保留原字节，检查器会提示。
- The 120 nonempty animation definitions with a local PNG have valid frame dimensions, positive default frame times and in-range frame indexes. `ae2/textures/block/crg_emissive.png.mcmeta` intentionally uses the PNG supplied by installed AE2 15.4.12 rather than a local copy.
- 具有本地 PNG 的 120 份非空动画定义，其帧尺寸、默认帧时长和帧索引检查通过。`ae2/textures/block/crg_emissive.png.mcmeta` 使用已安装 AE2 15.4.12 提供的 PNG，不需要包内重复提供贴图。

`python package.py --check` checks the source tree without writing output. A verification ZIP was written outside `dist/`, then v1.2.8 was packaged separately; published v1.2.7 artifacts were not replaced. Temporary fixtures confirmed rejection of missing files, changed hashes, duplicate JSON keys, truncated PNGs and output inside `pack/`. A simulated ZIP verification failure preserved the existing destination.

`python package.py --check` 检查源码树而不写产物。核对用 ZIP 写入 `dist/` 外，再单独打包 v1.2.8；未替换已发布 v1.2.7 成品。临时样本验证了缺文件、哈希不符、JSON 重复键、PNG 截断及输出到 `pack/` 均会被拒绝；模拟 ZIP 验证失败后，已有目标保持原样。

## Resource references / 资源引用

Reference: the installed Minecraft 1.20.1 instance, including AE2 15.4.12, ExtendedAE 1.4.22, AE2 Lightning Tech 2.1.4 and AE2 Insert Export Card 1.3.0. The scan indexed 196 installed mod JARs and 98 nested JARs. All 363 screen include references resolve within the pack after applying relative paths. Model, blockstate and texture references were compared against the pack and these JARs; generic Minecraft resources and runtime-generated models require their supplying game/loader code.

参照实际安装的 Minecraft 1.20.1 实例，包括 AE2 15.4.12、ExtendedAE 1.4.22、闪电科技 2.1.4 和 AE2 Insert Export Card 1.3.0。索引了 196 个模组 JAR 及 98 个嵌套 JAR。363 条界面 include 引用按相对路径解析后全部存在于包内。模型、方块状态和纹理引用与资源包及这些 JAR 对照；原版通用资源、运行时生成模型仍需结合游戏及加载器代码判断。

Static scanning initially left 15 distinct targets unresolved. They are classified below, rather than treating every missing JSON/PNG in this pack as a broken resource. Paths below are relative to `pack/assets/` unless marked as resource IDs.

静态扫描最初留下 15 个不同的未解析目标，逐项分类如下，不能把包内未提供的每个 JSON/PNG 都当作损坏。下方路径相对于 `pack/assets/`，资源 ID 除外。

| Target / 目标 | Referencing resource / 引用文件 | Classification / 分类 |
| --- | --- | --- |
| `ae2:block/crafting/monitor_formed` | `ae2/blockstates/crafting_monitor.json` | The installed AE2 blockstate also uses this target; `appeng.init.client.InitBuiltInModels` registers it in code. / 已安装 AE2 的原始方块状态同样引用它，由 `InitBuiltInModels` 代码注册。 |
| `forge:item/bucket` | `advanced_ae/models/item/quantum_infusion_bucket.json` | Present in Forge 1.20.1-47.4.0 injected runtime JAR. / 存在于 Forge 运行库，非缺失资源。 |
| `ae2:block/security_station_off` | `ae2/models/item/security_station.json` | Legacy security-station item overlay; installed AE2 15.4.12 contains no `security_station` class constants or corresponding model. / 遗留安全终端物品覆盖，当前 AE2 无对应资源及类常量。 |
| `expatternprovider:block/mddyue` | `expatternprovider/blockstates/mddyue.json` | Legacy blockstate; installed ExtendedAE 1.4.22 contains no `mddyue` resource or class constants. / 遗留方块状态，当前 ExtendedAE 无对应资源及类常量。 |
| `ae2importexportcard:item/import_card` (texture / 贴图) | `ae2insertexportcard/models/item/import_card.json` | Legacy import-card model; installed 1.3.0 supplies `insert_card` and `export_card`, with no `import_card` class constants or resources. / 当前附属使用 insert/export，未提供此遗留 import 物品。 |
| `extendedae_plus:block/crafting/4x_accelerator_formed_v2`, `16x_accelerator_formed_v2`, `64x_accelerator_formed_v2`, `256x_accelerator_formed_v2`, `1024x_accelerator_formed_v2` | The five matching `extendedae_plus/blockstates/*x_crafting_accelerator.json` files / 对应五个方块状态文件 | ExtendedAE Plus is not installed in the reference instance; these five targets cannot be verified against its runtime. / 参照实例未安装该附属，五个目标缺少运行基准，保留覆盖。 |
| `elementalcraft:block/iron`, `block/whiterock`, `block/container`, `block/container_top` (textures / 贴图) | `appelem/models/block/me_element_container.json` | Applied Energistics Elemental and ElementalCraft are absent; these four targets need those mods. / 实例未安装对应附属及 ElementalCraft，四个目标需由其提供。 |
| `ae2things:model/drive/cells/disk_1k` (texture / 贴图) | 23 models under `ae2additions/models/block/drive/cells/` / 该目录下 23 个模型 | AE Additions and AE2 Things are absent; compatibility with a specific pair of versions remains unverified. / 实例未安装两个相关附属，特定版本组合仍待核对。 |

AE2 `_color_` and `_channels_` texture placeholders were also classified as templates, not literal missing PNGs. Optional and legacy overlays were retained because this maintenance pass has no evidence that deleting them improves compatibility across supported installations. No game was launched; this is a static integrity check, not an in-game visual acceptance or a guarantee for uninstalled addon versions.

AE2 的 `_color_`、`_channels_` 纹理占位符也按模板处理，不能视作字面 PNG 缺失。本次保留可选附属及遗留覆盖，没有证据表明删除它们能改善不同安装组合的兼容性。未启动游戏；这是静态完整性检查，不是实机画面验收，也不保证未安装附属版本的兼容性。
