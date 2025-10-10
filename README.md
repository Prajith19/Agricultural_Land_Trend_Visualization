# Agricultural_Land_Trend_Visualization

Interactive D3.js visualization of **agricultural land area (sq. km)** across countries.

- **Line chart (1980–2020):** starts with the 5 biggest growth countries; add any country to compare.
- **Y-axis zoom & vertical pan:** buttons for zoom in/out/reset, plus **Shift + scroll** to pan through large values.
- **2020 ranking bar chart:** starts with top 5 countries; add up to 10 to compare (independent from the line chart).

---

## Why this project?

Agricultural land is a key indicator of land use and sustainability. This tool makes it easy to explore long-term trends, compare countries, and zoom/pan the scale to inspect both very large and smaller countries without losing detail.

---

## Demo (Local)

Serve the folder with a static server (browsers block local `file://` CSV loads):

```bash
# Python
python3 -m http.server 8000

# or Node
npx http-server -p 8000

