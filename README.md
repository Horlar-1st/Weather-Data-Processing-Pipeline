# 🌦️ Weather Data Cleaning and Processing

## 📌 Overview

This repository contains a simple data engineering pipeline developed as part of a take-home intern assignment for **Shega**. The pipeline ingests, cleans, transforms, and analyzes weather data from a CSV file, and outputs the processed results in CSV format along with a summary report and optional visualizations.

---

## 🧰 Tools and Technologies

- **Programming Language**: Python 3.x  
- **Libraries Used**:  
  - `pandas` – for data ingestion, cleaning, transformation  
  - `numpy` – for numerical operations  
  - `matplotlib` / `seaborn` – for visualization  
- **Input Format**: CSV  
- **Output Formats**: CSV

---

## 📂 Project Structure
```
weather-data-pipeline/
│
├── data/
│ └── weather_data.csv # Original input file
│
├── outputs/
│ ├── transformed_weather_data.csv  # Cleaned & transformed weather data
│ ├── top_5_hottest_cities.md       # (Optional) Top 5 hottest cities
│ └── avg_temp_bar_chart.png        # (Optional) Bar chart of avg temperatures
│
├── main.ipynb                # Main Python notebook
├── main_script.py            # Main Python script
├── requirements.txt.         # Python dependencies
└── README.md # This file
```
