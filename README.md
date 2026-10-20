# AE2 & Addons Texture Backport

AE2 及附属高版本材质移植，适用于 Minecraft 1.20.1。当前资源包版本：**1.2.0**。

本仓库保存已合并资源包的可编辑文件。GUI 主要来自 AE-Light-UI，量子计算机世界材质与效果结合 AE2LightMode，并针对部分高版本物品材质和模型进行修正。它不是所有高版本资源的逐字节完整移植；差异见核对报告。

1.1.3 删除四个非法资源文件，并将资源包显示说明改为英文。`audit/1.1.2/` 是旧版本快照；本次变更见 [1.1.3 清理说明](docs/1.1.3-资源清理.md)。

## 安装

下载本仓库 Release 附件 ZIP，放入游戏实例的 `resourcepacks` 文件夹并启用。停用之前的合并包及两个来源包，避免覆盖冲突。

需要配套 **AE2 Light UI Compat 1.2.0**，同时替换模组 JAR 与资源包 ZIP。本次恢复 AdvancedAE 高版本原始材质并修复合成状态页与便携元件染色，详见 [中英文更新说明](docs/releases/1.2.0.md)。请从 [v1.2.0 Release](https://github.com/yxchen-leo/AE2-Addons-Texture-Backport/releases/tag/v1.2.0) 下载 ZIP。历史附属支持核对见 [1.1.2 报告](docs/1.1.2-完整核对.md)，本次资源验证见 `audit/1.2.0/validation.json`。

## 文件说明

- `pack/`：完整可编辑资源包，包含原有署名和许可证文件。
- `CREDITS.txt`：来源与修改历史；其中旧命名空间属于历史记录，1.0.3 已改为 `ae2lightuicompat`。
- `file-provenance.json`：逐文件来源及校验值。
- `sources/`：移植物品及修正材质的来源清单，不包含完整第三方模组 JAR。
- `docs/`：安装说明及 1.0.2 材质核对报告。历史报告保留原版本号；1.0.3 仅更改专用按钮贴图命名空间，材质字节保持不变。
- `package.py`：将 `pack/` 打包为可安装 ZIP，运行 `python package.py`，输出位于 `dist/`。

## 许可与公开分发

本仓库暂为私有，**尚未完成所有素材的公开再分发许可核对**。来源包 AE2LightMode-1.20.1-V1.0.6 未附带明确授权声明；其他来源也需要按文件及适用许可证核对。详情见 [许可核对记录](docs/许可核对.md)。

未给整个资源包套用 MIT 或其他统一许可；各素材仍受原作者许可约束。适配模组的 MIT 许可不覆盖本资源包。署名不等于分发授权，仓库私有也不代表获得了原作者授权。

This private repository contains the editable Minecraft 1.20.1 resource pack and provenance records. Redistribution permissions have not been fully verified. Original assets retain their respective licenses. This is an unofficial compatibility backport and does not imply endorsement by AE2 or add-on authors.
