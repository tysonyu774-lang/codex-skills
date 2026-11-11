# Shopify Review Bridge

可运行的保守准备版，Python 3.10+，仅标准库。复制整个目录到 `~/.codex/skills/shopify-review-importer` 即可被技能发现。

## 使用

```sh
python3 scripts/bridge.py --config config.example.json --input reviews.json --out runs/batch-001
python3 scripts/bridge.py --config config.example.json --url https://www.amazon.com/dp/B00006IEEU --out runs/probe
python3 -m unittest discover -s tests -v
```

输入 JSON 列表或 CSV；字段见 SKILL.md。CSV 的 images 单元格使用 JSON 数组。日期只接受可靠的 ISO 日期，其他日期先由采集代理核对转换并保留原始文字。输出 UTF-8 BOM CSV、batch.json（完整数据、图片及问题清单）、HTML 预览与 SQLite 台账。跨运行增量必须复用同一 out；exported 可再次准备，submitted/unknown/confirmed 禁止再次导出。没有稳定 ID 的评论按正文、作者、日期、评分、图片计算指纹，此时内容变化无法可靠识别为同一评论，需人工核对。

本版不执行自动网页下载、分页、图片下载或 Shopify Files 上传，也不自动核对目标已有评论。保存的 HTML 需由代理在页面内按评论容器提取为 JSON。图片公开性依赖采集代理提供的检查证据，脚本仅校验声明、关联与地址格式。本版 apply 命令明确拒绝：真实导入需已授权浏览器及后台日志核对。没有店铺凭证时交付 CSV 不代表导入成功。

## 官方格式（2026-11-11 核对）

- [Loox CSV](https://help.loox.io/support/solutions/articles/501000162508-importing-reviews-using-a-custom-file)：日期 YYYY-MM-DD，photo_url 逗号分隔，最多 5 张 JPG/JPEG/PNG，地址不能有扩展名后缀参数。后台 Manage Reviews → Import reviews → Custom File；导入后核对结果邮件及失败 CSV。
- [Loox API](https://help.loox.io/support/solutions/articles/501000356871-loox-reviews-api-and-webhooks)：只读，不提供创建接口。
- [Judge.me CSV](https://judge.me/help/en/articles/8415368-importing-reviews-using-judge-me-template)：日期 DD/MM/YYYY，picture_urls 逗号分隔，最多 5 张公开 JPG/JPEG/PNG；邮箱允许为空。curated=not-yet 待审、ok 发布、spam 隐藏。Settings → Import reviews → Import from apps → Judge.me format，核对 Reviews Import Log 及实际评论。

## 验证与限制

真实探测 Amazon B00006IEEU 产品页面可读，但未找到 review-image-tile，因此“评论→对应买家图片”未验证；Wayfair Brittany sofa mcll1082 链接被读取工具报告不可访问，未取得评论。没有配置获准的数据提供商或登录店铺；无法宣称链接采集、图片可访问性或最终入库已验证。未对平台使用条款完成确认，启用采集前应核对所选读取方式及复用权限。

目标仓库已确认： https://github.com/tysoncommerce/codex-skills 。技能放在根目录 shopify-review-importer/，真实数据和会话仅存放忽略的 runs/。

## 网站介绍文案

Shopify 评论采集与导入助手（Shopify Review Bridge）帮助商家将有权复用、确认属于同款商品的评论整理为 Loox 或 Judge.me CSV，保留原始评分、日期和买家图片关联，提供问题清单及导入预览。支持 JSON/CSV 文件整理，Amazon 与 Wayfair 链接可识别，自动评论及图片采集仍待验证。导入需目标店铺权限并通过插件后台完成，默认 Judge.me 待审；持续自动同步暂不提供。展示站与接收评论的 Shopify 店铺分别配置。

## 原始页面适配器

安装 `python3 -m pip install -r requirements.txt` 后可运行：

```sh
python3 scripts/sources.py --url SOURCE_URL --html saved.html --out runs/extracted
```

Amazon 适配器仅提取 `data-hook=review` 容器及容器内 review-image-tile；Wayfair 适配器仅提取明确 Review JSON-LD，不将商品图或汇总评分当成评论。图片先标为 needs_access_check，公开访问检查仍需采集代理完成。输出 reviews.json 可进入 prepare 流程。此适配器处理保存页面，不执行网络请求或动态分页。

后续验证：技能检查器已在隔离环境补齐 PyYAML，检查通过。Firecrawl 返回的 Amazon 结构化结果缺乏原始容器证据，已拒绝作为真实评论采用；保存原始页面经确定性适配器处理取得 0 条，状态 requires_user_input。Wayfair 测试链接返回 HTTP 404，不能将空评论解释为该商品没有评论。实时采集链路仍未验证成功。
