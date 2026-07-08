# Codex Skills

Tyson的 Codex skills 仓库，用于分享可安装到 Codex 的自定义技能。

## ads-monthly-report

`ads-monthly-report` 用于分析 Meta Ads / Google Ads 月度广告数据，并输出客户可读的广告月报、素材分析、优化建议和专业 HTML 报告。

适用场景：

- Meta Ads 月度数据复盘
- Google Ads 月度数据复盘
- Meta + Google 混合广告月报
- 广告系列表现分析
- 素材优缺点分析
- 下月预算和优化建议
- 客户版 HTML 报告生成

## shopify-gmc-feed-sop

`shopify-gmc-feed-sop` 用于把 Shopify 产品资料整理成适合 Google Merchant Center / Google Shopping / PMax 使用的 feed 字段，并检查标题、描述、SEO、URL、标签、GMC 分类和 custom labels。

适用场景：

- Shopify 产品导出表审核
- Google GMC feed 标题和描述优化
- Google Shopping / PMax 商品分组准备
- 产品标题、SEO Title、Meta Description 改写
- Google Product Category 检查
- `custom_label_0-4` 拆分和规范
- 商品落地页一致性检查

## 安装方法

1. 下载本仓库。
2. 将你需要的 skill 文件夹复制到你的 Codex skills 目录：

```text
~/.codex/skills/
```

3. 确认最终路径类似：

```text
~/.codex/skills/ads-monthly-report/SKILL.md
~/.codex/skills/shopify-gmc-feed-sop/SKILL.md
```

4. 重启 Codex 或开启新对话。

## 使用方法

```text
用 $ads-monthly-report 分析这份 Meta / Google Ads 月数据，输出 HTML 月报。
```

也可以先输出人工可修改草稿：

```text
用 $ads-monthly-report 分析这份广告数据，先输出适合复制到 Mac 备忘录/word修改的中文月报草稿。
```

修改后再生成最终 HTML：

```text
用 $ads-monthly-report 根据这份我修订后的月报终稿，生成专业营销公司风格 HTML 报告。
```

Shopify GMC feed SOP：

```text
用 $shopify-gmc-feed-sop 检查这份 Shopify 产品导出表，输出适合 Google GMC feed 的标题、描述、URL、custom labels 和问题清单。
```

## 注意

- 不要把客户数据、广告账号截图、API key、广告后台导出原始文件提交到这个仓库。
- 这个仓库只保存通用 skill 文件。
- 如果你更新了字段映射、报告结构或 feed SOP 规则，重新提交并推送即可。
