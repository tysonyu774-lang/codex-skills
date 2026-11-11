# TysonCommerce Skills

面向 Shopify 商家和数字营销团队的实用 AI 技能。官网：[tysoncommerce.com](https://tysoncommerce.com/) · GitHub：[tysoncommerce](https://github.com/tysoncommerce)

## 按用途选择

| 分类 | 技能 | 用途与输出 | 状态 |
|---|---|---|---|
| 广告分析与报告 | [ads-monthly-report](ads-monthly-report/SKILL.md) | 分析 Meta / Google Ads 月度数据，输出可修改中文草稿、素材分析、预算建议与 HTML 月报 | 已收录 |
| Shopify 商品与 Feed | [shopify-gmc-feed-sop](shopify-gmc-feed-sop/SKILL.md) | 审核产品数据，整理 GMC / Shopping / PMax 标题、描述、URL、分类与 custom labels | 已收录 |
| Shopify 评论管理 | [shopify-review-importer](https://github.com/tysoncommerce/codex-skills/pull/1) | 整理获准复用的评论，生成 Loox / Judge.me CSV、预览及问题清单 | 草稿 PR；尚未合并 |

“已收录”表示技能已在主分支，不代表对所有店铺或数据完成真实验证。评论工具当前支持文件准备与保存页面解析；Amazon / Wayfair 自动采集及真实店铺导入仍待验证。

## 安装

下载本仓库，将所需技能文件夹复制到本机的 Codex 技能目录：

```text
~/.codex/skills/ads-monthly-report/SKILL.md
~/.codex/skills/shopify-gmc-feed-sop/SKILL.md
```

重新开启对话；若未发现技能，重启应用。评论技能目前需从 feat/shopify-review-importer 分支获取，先阅读其使用说明。

也可以在支持技能安装的对话中发送：

```text
帮我安装 https://github.com/tysoncommerce/codex-skills 中的 ads-monthly-report 技能。
```

本仓库分发技能文件，尚未提供独立的一键安装插件。

## 对话使用示例

### 广告分析与报告

```text
用 $ads-monthly-report 分析这份 Meta / Google Ads 月数据，先输出可修改的中文月报草稿。
```

人工修订后：

```text
用 $ads-monthly-report 根据这份修订终稿生成专业 HTML 月报。
```

### Shopify 商品与 Feed

```text
用 $shopify-gmc-feed-sop 检查这份 Shopify 产品导出表，整理 GMC 标题、描述、URL、custom labels 和问题清单。
```

### Shopify 评论管理（草稿版）

```text
用 $shopify-review-importer 整理这份评论文件，关联到我指定的 Shopify 商品，生成 Judge.me 待审导入文件。
```

## 仓库组织与数据边界

每个技能保留独立根目录，以 SKILL.md 作为入口；按用途在本页分类，保持已有安装路径。脚本、参考资料和测试放在各自技能内。私有 shopify-daily-report-agent 是独立应用，不属于本技能目录。

仅提交通用代码、说明与明确标注的合成测试。客户数据、真实评论、截图、图片、登录会话、密钥和后台原始导出不进入仓库。店铺操作需要对应授权；生成文件不等于导入成功。
