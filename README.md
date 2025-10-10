# Agricultural_Land_Trend_Visualization

Interactive **D3.js** visualization of **Agricultural land (sq. km)** across countries.
It highlights top growth from **1980–2020** with an add-to-compare **line chart** (with **Y-axis zoom + vertical pan**) and an independent **bar chart** showing the largest agricultural-land holders in **2020**.

---

## Why this project?

Agricultural land is a key indicator of land use and sustainability. This tool makes it easy to:

* Explore long-term trends
* Compare countries interactively
* Zoom/pan the Y-axis to inspect both very large and smaller countries without losing detail

---

## Features

* **Line chart (1980–2020):** starts with the 5 biggest growth countries; add any country to compare.
* **Y-axis zoom & pan:** buttons for zoom **+ / − / 100%**, plus **Shift + Mouse-wheel** to pan vertically through huge values.
* **Ranking bar chart (2020):** begins with top 5 countries; add up to **10** to compare (independent from the line chart).
* **Tooltips & labels**, responsive SVG, dark UI.
* **Vanilla setup:** No bundlers; just open via a simple static server.

---

## Data Source

* **World Development Indicators (WDI)** by **The World Bank**
* **Indicator:** *Agricultural land (sq. km)*
* **Code:** `AG.LND.AGRI.K2`
* **Catalog:** *World Development Indicators* (WDI)

> WDI updates periodically; you can refresh the CSV by re-downloading the dataset and rerunning the prep script.

---

## Get the Dataset & Build `Agriculture_Land_Large.csv`

1. **Download WDI (World Development Indicators)**

   * Go to the official World Bank *World Development Indicators* catalog page.
   * Click **Download Data** to get the full ZIP.

2. **Extract the ZIP**

   * After unzipping, you’ll see several folders/files.
   * Locate the folder named **`WDICSV`** .

3. **Organize files**

   * Create a working folder, e.g., `agri-land-data/`.
   * Move the entire **`WDICSV`** folder into this working folder.
   * Put **`DataFormation.py`** in the **same** working folder:

4. **(First time only) Install Python deps**

   ```bash
   # Optional virtual env
   python3 -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate

   pip install -U pandas numpy
   ```

5. **Run the preparation script**

   ```bash
   cd agri-land-data
   python DataFormation.py
   ```

   * The script reads `WDICSV.csv`, filters the **AG.LND.AGRI.K2** indicator, cleans/reshapes data, and limits the timeline to **1980–2020**.
   * On success, it writes **`Agriculture_Land_Large.csv`** to the **same** folder as `DataFormation.py`.

6. **Move the final CSV next to the web app**

   * Copy or move `Agriculture_Land_Large.csv` into the same directory as your `index.html`.

---


> Ensure **`Agriculture_Land_Large.csv`** is in the **same folder** as `index.html`.

---

## Run Locally

Browsers restrict local file access; serve via a simple static server:

```bash
# Option A: Python
python3 -m http.server 8000

# Option B: Node
npx http-server -p 8000
```

Then open: **[http://localhost:8000](http://localhost:8000)**

---

## How to Use

* **Add countries** with the country input above each chart.
* **Line chart Y-zoom:** click **+** / **−** / **100%**.
* **Line chart Y-pan:** hold **Shift** and **scroll** over the chart area.
* **Bars (2020):** add up to **10** countries (independent of the line selection).
* **Tooltips:** hover to see exact values.

---

## Data Preparation (what the script does)

* Extracts the **Agricultural land (sq. km)** indicator from WDI (`AG.LND.AGRI.K2`).
* Reshapes to a tidy format with columns:
  `Country Name`, `Country Code`, `Indicator Name`, `Indicator Code`, `Year`, `Agricultural land (sq. km)`.
* Cleans numeric fields and drops rows with missing/non-numeric values for the selected years.
* **Temporal focus:** 1980–2020 for the line chart;
  the bar chart uses **2020** or **latest available ≤ 2020** as a fallback.
* Exports **`Agriculture_Land_Large.csv`** (consumed by the web app).

---

## Tech Stack

* **D3.js v7** (SVG, scales, axes, transitions)
* **Vanilla HTML/CSS/JS** (no build step)
* **Python + pandas** (one-time data formation)

---

## Acknowledgments & Data License

* Data © **The World Bank** (*World Development Indicators*).
* Please follow the World Bank’s data terms and attribution guidelines when using or sharing results.

---

