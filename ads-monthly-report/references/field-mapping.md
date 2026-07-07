# Field Mapping

Use this reference to normalize Meta Ads and Google Ads exports. Column names vary by locale; match case-insensitively and tolerate punctuation differences.

## Canonical Columns

Required whenever available:

- `platform`: Meta, Google, Mixed, or source-derived.
- `date` or `month`: report period.
- `campaign`: campaign name.
- `group`: ad set, ad group, asset group, or audience group.
- `ad`: ad name, creative name, asset name, keyword, or placement.
- `spend`
- `impressions`
- `clicks`
- `conversions`
- `revenue`
- `ctr`
- `cpc`
- `cpm`
- `cvr`
- `cpa`
- `roas`

## Meta Ads Common Column Names

- Campaign: `Campaign name`, `Campaign`, `广告系列名称`
- Ad set: `Ad set name`, `Ad Set`, `广告组名称`
- Ad: `Ad name`, `Ad`, `广告名称`
- Spend: `Amount spent`, `Spend`, `花费`, `金额花费`
- Impressions: `Impressions`, `展示次数`
- Clicks: `Link clicks`, `Clicks`, `点击量`, `链接点击`
- CTR: `CTR`, `Link CTR`, `点击率`
- CPC: `CPC`, `Cost per link click`, `单次点击费用`
- CPM: `CPM`, `Cost per 1,000 impressions`, `千次展示费用`
- Conversions: `Purchases`, `Results`, `Website purchases`, `转化`, `购买`
- CPA: `Cost per purchase`, `Cost per result`, `单次结果费用`
- Revenue: `Purchase conversion value`, `Conversion value`, `购买转化价值`
- ROAS: `Purchase ROAS`, `Website purchase ROAS`, `ROAS`

## Google Ads Common Column Names

- Campaign: `Campaign`, `Campaign name`, `广告系列`
- Ad group: `Ad group`, `Ad group name`, `广告组`
- Asset group: `Asset group`, `Asset group name`, `素材资源组`
- Ad/Asset: `Ad`, `Asset`, `Headline`, `Keyword`, `Search keyword`
- Spend: `Cost`, `Spend`, `费用`
- Impressions: `Impr.`, `Impressions`, `展示次数`
- Clicks: `Clicks`, `点击次数`
- CTR: `CTR`, `点击率`
- CPC: `Avg. CPC`, `Average CPC`, `平均每次点击费用`
- CPM: `Avg. CPM`, `Average CPM`, `平均每千次展示费用`
- Conversions: `Conversions`, `Conv.`, `转化次数`
- CPA: `Cost / conv.`, `Cost per conversion`, `每次转化费用`
- Revenue: `Conv. value`, `Conversion value`, `转化价值`
- ROAS: `Conv. value / cost`, `ROAS`

## Metric Formulas

Use these only when component metrics exist:

- CTR = clicks / impressions
- CPC = spend / clicks
- CPM = spend / impressions * 1000
- CVR = conversions / clicks
- CPA = spend / conversions
- ROAS = revenue / spend

Guard denominators. If denominator is zero or missing, leave the metric blank and note the caveat.

## Data Quality Flags

Flag these in the report:

- Missing spend, clicks, impressions, conversions, or campaign names.
- ROAS requested but revenue/conversion value missing.
- Multiple currencies without exchange rates.
- Date range absent or mixed.
- Rows with spend but no impressions or clicks.
- Duplicated platform/campaign/group/ad/date rows.
