ChatGPT said:
Agricultural_Land_Trend_Visualization

Interactive D3.js visualization of agricultural land area (sq. km) across countries.
It highlights top growth from 1980–2020 with an add-to-compare line chart (now with Y-axis zoom + vertical pan) and an independent bar chart showing the largest agricultural land holders in 2020.

Why this project?

Agricultural land is a key indicator of land use and sustainability. This tool makes it easy to explore long-term trends, compare countries, and zoom/pan the scale to inspect both very large and smaller countries without losing detail.

Features

Line chart (1980–2020): starts with the 5 biggest growth countries; add any country to compare.

Y-axis zoom & pan: buttons for zoom in/out/reset, plus Shift + scroll to pan vertically through huge values.

Ranking bar chart (2020): begins with top 5 countries; add up to 10 to compare (independent from the line chart).

Tooltips & labels for precise values, responsive SVG, dark UI.

Data Preparation (done by me)

Source: World Development Indicators (WDI) by The World Bank.
Original catalog: World Development Indicators

Steps I performed:

Extracted the agricultural land indicator (sq. km) from the full WDI dataset.

Filtered and reshaped to a tidy format with columns: Country Name, Country Code, Indicator Name, Indicator Code, Year, Agricultural land (sq. km).

Temporal focus: limited to 1980–2020 for the line chart (the bar chart uses 2020 or latest available ≤ 2020 as a fallback).

Cleaned numeric fields and dropped rows with missing/non-numeric values for the selected years.

Exported final CSV used by the app: e.g., Agriculture_Land_Large.csv.

Note: WDI updates periodically; rerun the prep script to refresh the CSV when new data is released.

Tech Stack

D3.js v7 (SVG, scales, axes, transitions)

Vanilla HTML/CSS/JS (no build step)

Run Locally

Because browsers restrict local file access, serve via a simple static server:

# Python
python3 -m http.server 8000

# or Node
npx http-server -p 8000


Then open: http://localhost:8000
Ensure Agriculture_Land_Large.csv is in the same directory as index.html.

How to Use

Add countries with the input above each chart.

Line chart Y-zoom: click + / − / 100%.

Line chart Y-pan: hold Shift and scroll over the chart area.

Bars: add up to 10 countries (independent of the line selection).

Acknowledgments & Data License

Data © The World Bank (World Development Indicators). Please follow the World Bank’s data terms and attribution guidelines when using or sharing results.
