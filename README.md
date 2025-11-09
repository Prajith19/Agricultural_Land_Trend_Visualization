````md
# Agricultural_Land_Trend_Visualization

[![Live Demo](https://img.shields.io/badge/Live%20Demo-bit.ly%2Fagrilandviz-2ea44f?logo=google-chrome&logoColor=white)](https://bit.ly/agrilandviz)
[![Hosted on AWS Amplify](https://img.shields.io/badge/Hosted%20on-AWS%20Amplify-FF9900?logo=awsamplify&logoColor=white)](https://staging.dw77vepfrd618.amplifyapp.com/)

**Live demo links**
- Amplify: https://staging.dw77vepfrd618.amplifyapp.com/  
- Short link: **https://bit.ly/agrilandviz**

**QR (clickable)**  
[![QR: bit.ly/agrilandviz](assets/qr-agrilandviz.png)](https://bit.ly/agrilandviz)

Interactive D3.js visualization of agricultural land area (sq. km) across countries.
It highlights top growth from 1980–2020 with an add-to-compare line chart (now with **Y-axis zoom + vertical pan**) and an **independent bar chart** showing the largest agricultural land holders in 2020.

---

## Why this project?

Agricultural land is a key indicator of land use and sustainability. This tool makes it easy to explore long-term trends, compare countries, and zoom/pan the scale to inspect both very large and smaller countries without losing detail.

---

## Features

* **Line chart (1980–2020):** starts with the 5 biggest growth countries; add any country to compare.
* **Y-axis zoom & pan:** buttons for zoom in / out / reset, plus **Shift + scroll** to pan vertically through huge values.
* **Ranking bar chart (2020):** begins with top 5 countries; add up to 10 to compare (**independent** from the line chart).
* **Tooltips & labels** for precise values, **responsive SVG**, **dark UI**.
* **Vanilla stack:** D3 v7 + HTML/CSS/JS (no build step).

---

## Data Source

* **Catalog:** World Development Indicators (WDI) — The World Bank  
  Link: https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators
* **Indicator used:** Agricultural land (sq. km).
* **Temporal focus:** 1980–2020 for the line chart; bar chart uses 2020 (or latest available ≤ 2020 as a fallback).

> WDI updates periodically; re-run the prep script to refresh the CSV when new data is released.

---

## Getting the Dataset & Preparing the CSV (Step-by-Step)

1. **Download WDI CSV package**
   * Go to the WDI catalog page above and download the **CSV** package (a zip archive).

2. **Extract the archive**
   * Unzip the downloaded file.
   * Inside, locate **`WDICSV.csv`** (this is the *only* file you need).

3. **Create a working folder**
   * Make a new folder (e.g., `wdi-agri-land/`).
   * Copy **`WDICSV.csv`** into this folder.
   * Place **`DataFormation.py`** in the **same** folder.

4. **Run the data formation script**
   * Requirements: Python 3.9+ and `pandas` installed.
   * From the folder containing both files, run:
     ```bash
     python3 DataFormation.py
     ```
   * Output: **`Agriculture_Land_Large.csv`** in the **same** folder.

5. **Move assets for the app**
   * Ensure **`Agriculture_Land_Large.csv`** is deployed with the app and accessible at  
     `DataSets/Agriculture_Land_Large.csv` (i.e., next to `index.html` inside a `DataSets/` folder).

**That’s it — the visualization is now ready to run.**

> If you keep everything flat (same directory), that also works. Just be sure `index.html` and `Agriculture_Land_Large.csv` end up together.

---

## Run Locally

Because browsers restrict local file access, serve via a simple static server:

```bash
# Python
python3 -m http.server 8000

# or Node
npx http-server -p 8000
````

Then open: **[http://localhost:8000](http://localhost:8000)**
Ensure **`DataSets/Agriculture_Land_Large.csv`** is in the **same directory** as `index.html`.

---

## Hosting & Deployment

This project is hosted on **AWS Amplify (Drag-and-Drop Hosting)** and the public URL is shortened with **Bitly**.

**Deploy steps used**

1. Create a folder:

   ```
   site/
     index.html
     DataSets/
       Agriculture_Land_Large.csv
     (any other assets referenced by index.html)
   ```
2. **Zip the *contents* of `site/`** (so the ZIP root has `index.html`, not `site/index.html`).
3. AWS Console → **Amplify Hosting** → **Host your web app** → **Deploy without Git provider** → **Drag & drop** the ZIP.
4. Wait for status **Deployed** → live at
   `https://staging.dw77vepfrd618.amplifyapp.com/`.

**Short link**

* Created in Bitly with custom back-half **`agrilandviz`** → **[https://bit.ly/agrilandviz](https://bit.ly/agrilandviz)**

---

## How to Use

* **Add countries** with the input above each chart.
* **Line chart Y-zoom:** click **+ / − / 100%**.
* **Line chart Y-pan:** hold **Shift** and **scroll** over the chart area.
* **Bar chart (2020):** add up to **10 countries** to compare (independent of the line selection).
* **Tooltips** show precise values on hover.

---

## Data Preparation (what the script does)

* Extracts the **Agricultural land (sq. km)** indicator from the full WDI table.
* Filters & reshapes to a tidy format with columns:
  `Country Name`, `Country Code`, `Indicator Name`, `Indicator Code`, `Year`, `Agricultural land (sq. km)`.
* Limits the line chart window to **1980–2020** (bar chart uses **2020** or latest ≤ 2020).
* Cleans numeric fields and drops missing/non-numeric values for the selected years.
* Exports **`Agriculture_Land_Large.csv`** consumed by the D3 app.

---

## Tech Stack

* **D3.js v7** (SVG, scales, axes, transitions)
* **Vanilla HTML/CSS/JS** (no build step, easy to host)

---

## Acknowledgments & Data License

* **Data © The World Bank (World Development Indicators).**
  Please follow the World Bank’s data terms and attribution guidelines when using or sharing results.
  Catalog link: [https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators](https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators)

```
```
