
# Nairobi Drainage Analysis

**Nairobi Drainage Analysis** is an interactive **Streamlit dashboard** that helps city planners, engineers, and utility agencies in **Nairobi, Kenya** monitor drainage systems, assess flood risk, and prioritize maintenance actions for urban drains.

This project combines historical rainfall data, neighborhood demographics, drainage network status, and past flood reports to generate actionable insights and visualizations.

---

## 🚀 Features

* 🌍 **Overview Dashboard** showing key flood risk & drainage metrics
* 📊 **Flood Risk Assessment** by neighborhood
* 🛠 **Drainage Priority Scoring** to identify drains needing urgent maintenance
* 📍 **Interactive Maps** (Plotly & Mapbox) of risk and priority scores
* 📈 **Data Tables** and summaries for analysis

---

## 📁 Project Structure

```
Nairobi_Drainage_Analysis/
├── dashboard/
│   └── app.py                # Main Streamlit app
├── src/
│   ├── flood_risk.py         # Flood risk scoring logic
│   └── drainage_priority.py  # Drainage priority scoring logic
├── data/
│   ├── neighborhoods.csv     # Neighborhood list & metadata
│   ├── rainfall.csv          # Rainfall observations
│   ├── flood_reports.csv     # Flood history
│   └── drainage.csv          # Drainage system data
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 🧠 How It Works

The dashboard has three main sections:

### 📌 Overview

Shows a quick summary of:

* Total number of neighborhoods
* Highest flood risk
* Number of drains monitored
* Top drainage priority scores

### 🌧 Flood Risk Tab

This tab ranks neighborhoods on a **flood risk score** based on:

* Average rainfall (mm)
* Historical flood count
* Population density
* Blockage indicators (where available)

### 🚧 Drainage Priority Tab

Identifies drains needing maintenance using:

* Blockage score
* Neighborhood flood risk
* Drain length

---

## 🧾 Requirements

This project uses the following Python packages:

```
streamlit
pandas
numpy
plotly
```

Install them via:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

Before running, make sure you have the required CSV dataset files in the `data/` folder (e.g., `neighborhoods.csv`, `rainfall.csv`, `drainage.csv`, and `flood_reports.csv`).

To start the dashboard:

```bash
streamlit run dashboard/app.py
```

This will launch a browser window with the interactive dashboard.

---

## 🛠 Usage Tips

* Use the **sidebar filters** to narrow analysis to specific neighborhoods
* View **top risk and priority tables** for high‑risk zones
* Explore the **map visualizations** for spatial patterns

---

## 📊 Example Code Snippets

### Calculate Flood Risk

```python
from src.flood_risk import calculate_flood_risk

df = calculate_flood_risk()
```

### Calculate Drainage Priority

```python
from src.drainage_priority import calculate_drainage_priority

priority_df = calculate_drainage_priority()
```

---

## 📦 Contributing

Contributions are welcome! Please fork the repo and submit a pull request with improvements such as:

* Support for updated or real-time rainfall data
* Integration with GIS databases
* Better UI/UX for the dashboard

---

