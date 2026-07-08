---
name: shopify-gmc-feed-sop
description: Use when auditing, rewriting, or preparing Shopify product data for Google Merchant Center, Google Shopping, PMax, Shopping ads, SEO product titles, meta descriptions, product descriptions, product URLs, Shopify tags, Google Product Category, and GMC custom_label_0-4 fields. Trigger for Shopify product upload SOPs, product feed optimization, multilingual market feed checks, feed disapprovals, title/description consistency checks, or requests to turn product info into a GMC-ready feed table.
---

# Shopify GMC Feed SOP

## Overview

Use this skill to turn Shopify product information into Google Merchant Center-ready feed fields. The goal is not merely to upload products; the goal is to make shoppers, Google Shopping, Google Ads, PMax, SEO, and feed segmentation understand the same product in a consistent way.

For detailed field rules and templates, read `references/feed-rules.md` before auditing or rewriting product fields.

## Workflow

1. Identify the target market: country, language, brand, product type, and whether products are custom-made or ready-to-ship.
2. Collect the base product facts before writing: collection, style/model name, product type, material, functions, color, installation or fit method, use scenario, customization, target country, target language, and brand.
3. Build the keyword set before writing titles:
   - Core product term: what the product is.
   - Function terms: what it does.
   - Material/style terms: what it is made of or looks like.
   - Scenario terms: where or how it is used.
4. Rewrite or audit the Shopify product title, SEO title, meta description, product description, URL handle, Shopify tags, Google Product Category, and custom labels.
5. Check landing page consistency: title, description, price, color, inventory, product attributes, country, and language must match the product page.
6. Return a client-ready output: either a concise audit, a corrected feed table, or a product upload checklist, depending on the user's request.

## Output Patterns

When the user provides one or more products, prefer a table with these fields:

- product_name
- country
- language
- core_keyword
- function_terms
- material_terms
- scenario_terms
- shopify_title
- seo_title
- meta_description
- url_handle
- product_description
- shopify_tags
- google_product_category
- custom_label_0
- custom_label_1
- custom_label_2
- custom_label_3
- custom_label_4
- issues_found
- recommended_action

When the user asks for an audit, group findings by severity:

- Critical: likely policy, mismatch, disapproval, wrong language, wrong category, missing required feed fields.
- Important: weak keyword structure, poor title order, missing custom labels, thin descriptions, inconsistent labels.
- Nice to improve: readability, richer material details, cleaner tags, URL polish.

When data is incomplete, infer conservatively and mark assumptions clearly. Do not invent product claims, materials, discounts, guarantees, certifications, inventory, or shipping promises unless the user provides them or the landing page shows them.

## Required Checks

Always check these points before finalizing:

- The main keyword is placed near the front of the title.
- Title, description, SEO title, and landing page facts are consistent.
- No promotional wording is placed in product titles.
- The target language matches the target country.
- Product claims are supported by the product page or source data.
- Google Product Category is specific and consistent within the same product family.
- custom_label_0-4 have fixed meanings and consistent spelling.
- Image guidance is included when the request covers GMC readiness.

## Reference

Read `references/feed-rules.md` for:

- product fact checklist
- keyword categories
- title formula
- SEO title and meta description formula
- product description structure
- Shopify tag rules
- GMC custom_label_0-4 structure
- Google Product Category rules
- landing page and GMC post-sync checklist
