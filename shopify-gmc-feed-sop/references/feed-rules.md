# Shopify to Google GMC Feed Rules

## Purpose

Optimize Shopify product fields so Google Merchant Center, Google Shopping, Google Ads, PMax, SEO, and human shoppers receive a consistent and searchable product record.

## Core Principles

1. Define search terms before writing product titles.
2. Keep product title, SEO title, description, and landing page facts consistent.
3. Use fixed GMC custom labels instead of temporary naming.
4. Keep country, language, and product series naming consistent.
5. Never add unsupported claims, irrelevant high-volume keywords, mixed-language terms, or promotional wording in titles.

## Base Product Facts

Collect these facts before uploading or rewriting:

- product series or collection
- style/model name
- product type
- material
- key functions
- color
- installation, fit, or use method
- use scenario
- custom-made or ready-to-ship
- target country
- target language
- brand

Check whether the page actually shows each attribute, function, and material claim.

## Keyword Set

Each product should have four keyword groups:

- Core product term: defines what the product is.
- Function terms: define what it does.
- Material/style terms: define material, texture, finish, or visual style.
- Scenario terms: define where it is used.

Keep terms relevant to the target country and language. Use Google Ads Keyword Planner or source market research when available. Prefer high-search-volume terms only when they are highly relevant and supported by the product page.

Example German curtain terms:

- Core: `Vorhang nach Mass`, `Gardine nach Mass`, `Verdunkelungsvorhang nach Mass`
- Function: `blickdicht`, `verdunkelnd`, `transparent`, `schallabsorbierend`, `waermeisolierend`, `wetterfest`
- Material/style: `Leinenoptik`, `Samt`, `Polyester`, `strukturiertes Gewebe`
- Scenario: `Wohnzimmer`, `Schlafzimmer`, `Balkon`, `Outdoor`

Use ASCII transliterations when a downstream system may not handle special characters safely, but preserve the correct market language in final customer-facing fields if the store supports it.

## Shopify Product Title

Recommended format:

`Core Keyword - Style Name, Function Term & Function Term - Brand`

The title must include:

- one core product term
- style/model name
- one or two core function terms
- brand

Do not include:

- invented low-search terms
- unsupported claims
- mixed languages
- promotional words such as free shipping, lowest price, discount, sale
- all caps or exaggerated symbols

Examples:

- `Vorhang nach Mass - Lucca, blickdicht & verdunkelnd - BTTO`
- `Gardine nach Mass - Lucca, transparent & elegant - BTTO`
- `Verdunkelungsvorhang nach Mass - Lucca, blickdicht & schallabsorbierend - BTTO`

Product type templates:

- Custom blackout curtain: `Vorhang nach Mass - [Style], blickdicht & verdunkelnd - [Brand]`
- Custom sheer curtain: `Gardine nach Mass - [Style], transparent & elegant - [Brand]`
- Custom velvet curtain: `Samtvorhang nach Mass - [Style], blickdicht & weich fallend - [Brand]`
- Custom linen-look curtain: `Leinenvorhang nach Mass - [Style], natuerlich & blickdicht - [Brand]`
- Outdoor curtain: `Outdoor Vorhang nach Mass - [Style], wetterfest & blickdicht - [Brand]`

## SEO Title, Meta Description, URL

SEO title should usually match or closely follow the Shopify title:

`Core Keyword - Style Name, Function Term & Function Term - Brand`

Meta description rules:

- include the core keyword
- include one or two key benefits
- include material or customization information
- avoid keyword stuffing
- avoid promises not visible on the page
- keep the description clear and structured

Example:

`457gsm strukturiertes Gewebe, 90-95% Verdunkelung, 7 Farbvarianten. Vorhang nach Mass fuer moderne Raeume, massgefertigt in Deutschland mit kostenloser Lieferung und 5 Jahren Garantie.`

Only include free delivery, warranty, location, percentages, or other claims when verified in the source data or landing page.

URL handle rules:

- lowercase
- hyphen-separated
- not too long
- single target language
- prefer style name plus core function/product term

Examples:

- `/products/lucca-verdunkelungsvorhang`
- `/products/lucca-vorhang-nach-mass`

## Product Description

Recommended structure:

1. First sentence includes the core keyword.
2. Function benefits: e.g. blackout, light-filtering, sound-absorbing, soft drape.
3. Material explanation: e.g. weight, texture, durability, care.
4. Customization explanation: e.g. made-to-measure width and height.
5. Use scenarios: e.g. living room, bedroom, balcony, outdoor, large windows.

If the feed tool supports `product_highlight`, use three to five short high-value benefit lines for quick scanning.

## Shopify Tags

Shopify tags are for internal search, exports, automation, and feed mapping. Keep them short and consistent.

Recommended logic:

- country tag
- product attribute tag
- series tag
- style tag

Example:

- `de-custom`
- `de-blackout`
- `lucca`
- `custom-series`

Rules:

- use two to four core tags where possible
- avoid dozens of noisy tags
- keep naming consistent
- use consistent country abbreviations

## GMC Custom Labels

Use fixed meanings for Google Merchant Center custom labels:

- `custom_label_0` = country, e.g. `de`, `fr`, `nl`, `it`, `es`
- `custom_label_1` = sales method, e.g. `custom`, `ready`
- `custom_label_2` = product function, e.g. `blackout`, `sheer`, `outdoor`
- `custom_label_3` = material/style, e.g. `linen`, `velvet`, `polyester`
- `custom_label_4` = series/style, e.g. `lucca`, `milano`, `oslo`

Example:

- `custom_label_0 = de`
- `custom_label_1 = custom`
- `custom_label_2 = blackout`
- `custom_label_3 = linen`
- `custom_label_4 = lucca`

If a store currently uses combined Shopify tags such as `de-custom`, `de-blackout`, or `de-linen`, recommend keeping those as Shopify tags but splitting them into `custom_label_0-4` via feed app mapping or GMC attribute rules.

## Google Product Category

Choose the single most specific category that describes the product's primary function.

Rules:

- choose the most specific relevant category
- use primary product function, not secondary benefits
- keep the same product family consistent across countries and variants
- do not change category because of secondary features such as sound absorption or heat insulation

For curtain products, keep the category close to Curtains & Drapes / Window Treatments rather than unrelated categories.

## Landing Page Consistency

Before publishing or syncing, check:

- product title matches the page title and visible product facts
- description claims match page content
- price is consistent
- color is consistent
- inventory/availability is consistent
- custom or ready-to-ship status is consistent
- language and country match

## Post-Sync GMC Checks

After Shopify syncs to GMC:

1. Confirm product sync status in the feed app or Merchant Center.
2. Check title: core keyword first, page-consistent, no promo wording, no mixed languages.
3. Check description: complete, page-consistent, includes core attributes.
4. Check Google Product Category: specific and consistent.
5. Check custom labels: mapped to the correct 0-4 fields, no missing values, consistent spelling.
6. Check images: clean main image, no watermark, no collage text, product is clear, color is realistic.
7. Check GMC diagnostics: disapprovals, data quality warnings, title/description length issues, and missing fields.

## Suggested Deliverables

For product preparation:

- keyword matrix
- feed-ready product field table
- Shopify upload checklist
- GMC post-sync checklist

For existing feed audits:

- issue summary
- corrected titles and descriptions
- corrected custom labels
- landing page mismatch notes
- next actions for Shopify, SEO, and ads teams
