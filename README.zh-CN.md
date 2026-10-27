# AE2 及附属材质移植

已发布 **1.2.6**：ExtendedAE 物品与中文修复及 GUI 细节适配。请配套使用模组和资源包 **1.2.6**。见[更新说明](docs/releases/1.2.6.md)。

[English](README.md) | **简体中文**

适用于 **Minecraft 1.20.1 / Forge** 的 AE2 及附属材质与 GUI 移植资源包。

本仓库保存合并资源包的可编辑文件。GUI 主要来自 AE-Light-UI，量子计算机世界材质与效果结合 AE2LightMode，并包含部分高版本物品材质、模型与兼容修正。它不是全部高版本资源的完整移植，差异见各版本核对报告。

## 安装

1. 从 [v1.2.6](https://github.com/yxchen-leo/AE2-Addons-Texture-Backport/releases/tag/v1.2.6) 下载 ZIP，放入 `resourcepacks` 并启用。
2. 同时安装 **AE2 Light UI Compat 1.2.6** JAR，放入 `mods`。
3. 移除旧版 JAR，停用旧版合并包及两个来源包，重启客户端。

v1.2.1 起由已安装模组提供 GuideME 手册；v1.2.2 仅为 ExpandedAE 的两张错误页面提供修正覆盖。mekmm 战利品修复位于配套 JAR 中，单独启用 ZIP 不会修改服务端战利品。单人游戏安装客户端 JAR 即可；独立服务器需安装 JAR 才能启用战利品修复。

## 文件说明

- `pack/`：可编辑资源包，包含署名和许可文件。
- `CREDITS.txt`：来源与修改历史；旧命名空间自 1.0.3 起改为 `ae2lightuicompat`。
- `file-provenance.json`：逐文件来源与 SHA-256。
- `sources/`：来源与改动清单，不包含完整第三方模组 JAR。
- `docs/`、`audit/`：版本说明与核对报告；历史报告仅对应其标注的版本。
- `package.py`：运行 `python package.py`，在 `dist/` 生成 ZIP。

历史支持范围见 [1.1.2 核对报告](docs/1.1.2-完整核对.md)，v1.2.1 静态核对见 [核对记录](audit/1.2.1/validation.json)。编译和静态核对不代表游戏内画面验收，具体范围见各版本说明。

## 许可与公开分发

仓库保持私有，**尚未完成全部第三方素材的公开再分发许可核对**。来源包 AE2LightMode-1.20.1-V1.0.6 未附明确授权声明，其他来源也需按文件核对。详情见 [许可记录](docs/许可核对.md)。

素材保留原作者许可；适配模组的 MIT 许可不覆盖本资源包。署名或仓库私有均不等于获得再分发授权。本项目为非官方兼容移植，不代表 AE2 或附属作者认可。
