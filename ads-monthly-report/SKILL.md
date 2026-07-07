---
name: ads-monthly-report
description: Use when the user uploads or references Meta Ads, Facebook Ads, Instagram Ads, Google Ads, YouTube Ads, Performance Max, Search, Shopping, campaign, ad set, ad group, keyword, creative, or asset monthly performance data and wants a professional client-ready HTML report with campaign analysis, creative/material analysis, strengths, weaknesses, budget recommendations, and next-month optimization actions.
---

# Ads Monthly Report

## Purpose

Create a professional client-ready advertising monthly report from Meta Ads and/or Google Ads exports. The default deliverable is a polished standalone HTML page, plus optional zipped assets when useful.

## Trigger Examples

- "用这个 Meta 广告月数据输出 HTML 月报"
- "分析 Google Ads 月报，给客户版报告"
- "把 Meta 和 Google 广告数据合并分析，包含素材优缺点和优化方案"
- "根据广告系列、广告组、素材数据做一份月度复盘页面"

## Required Workflow

1. **Inventory inputs**
   - Identify file type: CSV, XLSX, TSV, screenshots, image/video thumbnails.
   - Identify platform and grain: Meta campaign/ad set/ad, Google campaign/ad group/keyword/asset.
   - If multiple files exist, preserve platform and source filename.

2. **Read references as needed**
   - Read `references/field-mapping.md` before normalizing columns.
   - Read `references/report-structure.md` before writing the HTML report.

3. **Normalize data**
   - Map source columns into canonical metrics: spend, impressions, clicks, CTR, CPC, CPM, conversions, CPA, revenue/value, ROAS.
   - Parse currency and percentages as numbers.
   - Keep platform, campaign, group, ad/creative, date/month, and source filename.
   - If a metric is missing, calculate it only when numerator and denominator are available.

4. **Validate data quality**
   - Check row counts, missing key columns, zero spend rows, duplicate rows, currency ambiguity, date range ambiguity, and inconsistent conversion definitions.
   - State caveats in the report. Do not hide missing revenue/ROAS data.

5. **Analyze**
   - Overall performance: spend, conversions, revenue, ROAS, CPA, CTR, CPC, CPM.
   - Platform comparison: Meta vs Google when both exist.
   - Campaign ranking: best/worst by spend efficiency and conversion volume.
   - Funnel diagnosis: traffic quality, click cost, conversion rate, CPA/ROAS.
   - Creative/material analysis: use ad names, asset names, copy labels, thumbnails, and available breakdowns.
   - Identify winners to scale, losers to pause, and uncertain tests needing more data.

6. **Generate deliverable**
   - Create `outputs/<descriptive-name>/index.html`.
   - If images/assets are included or generated, place them under `outputs/<descriptive-name>/assets/`.
   - Produce a zip package only when the user asks or when multiple report files need delivery.
   - The HTML must be standalone enough to open locally; external CDNs are allowed only when needed and must have graceful fallback.

## Report Requirements

The HTML report must include:

- Executive summary in Chinese by default unless user requests another language.
- KPI cards for spend, revenue, conversions, CPA, ROAS, CTR.
- Campaign performance table.
- Top winners and bottom underperformers.
- Creative/material analysis section.
- Strengths and weaknesses.
- Clear improvement plan for next month.
- Budget adjustment suggestions.
- Data caveats and source notes.

## Creative Analysis Rules

When creative fields are available:

- Group by ad name, creative name, asset name, image/video label, or headline.
- Evaluate creative using CTR, CPC, CVR, CPA, ROAS, and spend share.
- Label each creative as: Scale, Keep Testing, Refresh, Pause, or Needs More Data.
- Explain likely reasons in plain marketing language, not only metrics.

When thumbnails or screenshots are provided:

- Use visual inspection to comment on hook, offer, product visibility, text clarity, brand consistency, format, and mobile readability.
- Include thumbnails in the report only when the user provided them or they are locally available.

## Recommendation Style

Recommendations must be specific and operational:

- Good: "Increase budget 15-25% on Campaign A because ROAS is 3.8 with stable CPA and enough conversion volume."
- Bad: "Optimize campaign performance."

Use confidence language:

- High confidence: strong spend and conversion volume.
- Medium confidence: directional but limited volume.
- Low confidence: insufficient data or missing conversion/revenue fields.

## Output Naming

Use names like:

- `outputs/meta-google-ads-monthly-report-2026-06/index.html`
- `outputs/meta-ads-report-<month>.zip`

Final response should link only user-facing deliverables in `outputs/`.
