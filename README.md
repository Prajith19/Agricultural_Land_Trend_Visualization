````md
# Agricultural_Land_Trend_Visualization

<p align="left">
  <a href="https://bit.ly/agrilandviz">
    <img alt="Live Demo" src="https://img.shields.io/badge/Live%20Demo-Open%20App-2ea44f?logo=google-chrome&logoColor=white">
  </a>
  <a href="https://staging.dw77vepfrd618.amplifyapp.com/">
    <img alt="Hosted on AWS Amplify" src="https://img.shields.io/badge/Hosted%20on-AWS%20Amplify-FF9900?logo=awsamplify&logoColor=white">
  </a>
</p>

Interactive D3.js visualization of agricultural land area (sq. km) across countries.
It highlights top growth from **1980–2020** with an add-to-compare line chart (now with **Y-axis zoom + vertical pan**) and an **independent bar chart** showing the largest agricultural land holders in 2020.

**Live demo**
- Amplify URL: https://staging.dw77vepfrd618.amplifyapp.com/  
- Short link: **https://bit.ly/agrilandviz**

<!-- QR code (clickable) -->
<p align="left">
  <a href="https://bit.ly/agrilandviz">
    <img src="assets/qr-agrilandviz.png" alt="QR: bit.ly/agrilandviz" width="180" />
  </a>
  <br/>
  <sub>Scan or click to open: <a href="https://bit.ly/agrilandviz">bit.ly/agrilandviz</a></sub>
</p>

---

## Why this project?

Agricultural land is a key indicator of land use and sustainability. This tool makes it easy to explore long-term trends, compare countries, and zoom/pan the scale to inspect both very large and smaller countries without losing detail.

---

## Features

- **Line chart (1980–2020):** starts with the 5 biggest growth countries; add any country to compare.  
- **Y-axis zoom & pan:** buttons for zoom in / out / reset, plus **Shift + scroll** to pan vertically through huge values.  
- **Ranking bar chart (2020):** begins with top 5 countries; add up to 10 to compare (**independent** from the line chart).  
- **Tooltips & labels** for precise values, **responsive SVG**, **dark UI**.  
- **Vanilla stack:** D3 v7 + HTML/CSS/JS (no build step).

---

## Data Source

- **Catalog:** World Development Indicators (WDI) — The World Bank  
  Link: https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators
- **Indicator used:** Agricultural land (sq. km).
- **Temporal focus:** 1980–2020 for the line chart; bar chart uses 2020 (or latest available ≤ 2020 as a fallback).

> WDI updates periodically; re-run the prep script to refresh the CSV when new data is released.

---

## Getting the Dataset & Preparing the CSV (Step-by-Step)

1. **Download WDI CSV package**  
   Go to the WDI catalog page above and download the **CSV** archive.

2. **Extract the archive**  
   Unzip it and locate **`WDICSV.csv`** (this is the only file you need).

3. **Create a working folder**  
   Make a folder (e.g., `wdi-agri-land/`), copy **`WDICSV.csv`** into it, and place **`DataFormation.py`** there too.

4. **Run the data formation script**  
   Requirements: Python 3.9+ and `pandas`.  
   ```bash
   python3 DataFormation.py
````

Output: **`Agriculture_Land_Large.csv`** in the same folder.

5. **Move assets for the app**
   Ensure **`Agriculture_Land_Large.csv`** is deployed with the app and accessible at
   `DataSets/Agriculture_Land_Large.csv` (i.e., next to `index.html` inside a `DataSets/` folder).

---

## Run Locally

Serve via a simple static server (browsers block `file://` CSV requests):

```bash
# Python
python3 -m http.server 8000

# or Node
npx http-server -p 8000
```

Then open: **[http://localhost:8000](http://localhost:8000)**
Make sure `DataSets/Agriculture_Land_Large.csv` is in the expected location relative to `index.html`.

---

## Hosting & Deployment (AWS Amplify + short URL)

This project is hosted on **AWS Amplify (Drag-and-Drop Hosting)** and shortened with **Bitly**.

### A. Deploy steps (what I used)

1. Prepare a folder (e.g., `site/`) containing:

   ```
   site/
     index.html
     DataSets/
       Agriculture_Land_Large.csv
     (any other assets referenced by index.html)
   ```
2. **Zip the contents of `site/`** (so the ZIP root has `index.html`, not `site/index.html`).
3. AWS Console → **Amplify Hosting** → **Host your web app** → **Deploy without Git provider** → **Drag & drop** the ZIP.
4. Wait for status **Deployed**. The app is now live at
   `https://staging.dw77vepfrd618.amplifyapp.com/`.

> Notes:
> • If you change files later, upload a new ZIP in the same Amplify environment.
> • If CSV paths 404, verify `DataSets/Agriculture_Land_Large.csv` exists in the deployed bundle.

### B. Short link with Bitly

1. Create a Bitly account (free).
2. **Create new link** → Long URL: `https://staging.dw77vepfrd618.amplifyapp.com/`.
3. Set a custom back-half: `agrilandviz` → Save.
   Final short URL: **[https://bit.ly/agrilandviz](https://bit.ly/agrilandviz)**

> If `agrilandviz` is taken, Bitly will ask for a different back-half.

### C. Optional: move to your own domain later

* Buy a domain in Route 53 or use your existing registrar.
* In Amplify → **Domain management → Add domain**, map `yourdomain.com` (and `www`) to this app.
  Amplify will provision HTTPS automatically if the domain is in Route 53.

---

## How to Use

* **Add countries** with the input above each chart.
* **Line chart Y-zoom:** **+ / − / 100%** buttons.
* **Line chart Y-pan:** hold **Shift** and **scroll**.
* **Bar chart (2020):** add up to **10** countries; selection is independent of the line chart.
* **Tooltips** show precise values on hover.

---

## Data Preparation (what the script does)

* Extracts the **Agricultural land (sq. km)** indicator from WDI.
* Reshapes to tidy columns:
  `Country Name`, `Country Code`, `Indicator Name`, `Indicator Code`, `Year`, `Agricultural land (sq. km)`.
* Filters **1980–2020** for the line chart; bar chart uses **2020** (or latest ≤ 2020).
* Cleans numeric fields and removes missing rows.
* Outputs **`Agriculture_Land_Large.csv`** consumed by the D3 app.

---

## Tech Stack

* **D3.js v7**
* **Vanilla HTML/CSS/JS**

---

## Acknowledgments & Data License

* **Data © The World Bank (World Development Indicators)** — follow World Bank data terms and attribution.

```
```
