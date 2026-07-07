# HTML Report Notes

Use this as a lightweight implementation reminder for report output.

Recommended file layout:

```text
outputs/<report-name>/
├── index.html
├── assets/
│   ├── chart-*.svg or .png
│   └── creative-*.png
└── source-summary.json
```

Recommended HTML blocks:

- `.hero`
- `.kpi-grid`
- `.insight-card`
- `.chart-panel`
- `.data-table`
- `.recommendation-list`
- `.source-notes`

The HTML should include embedded CSS unless the report has many assets. Prefer simple SVG/CSS charts when possible.
