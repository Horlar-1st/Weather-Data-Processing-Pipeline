# 🌦️ Weather Data Processing Pipeline

## 📌 Overview

This repository contains a simple data engineering pipeline developed as part of a take-home intern assignment for **Shega**. The pipeline ingests, cleans, transforms, and analyzes weather data from a CSV file, and outputs the processed results in CSV format along with a summary report and optional visualizations.

---

## 🧰 Tools and Technologies

- **Programming Language**: Python 3.x  
- **Libraries Used**:  
  - `pandas` – for data ingestion, cleaning, transformation  
  - `numpy` – for numerical operations  
  - `matplotlib` / `seaborn` – (optional) for visualization  
- **Input Format**: CSV  
- **Output Formats**: CSV, TXT, PNG (optional)

---

## 📂 Project Structure

weather-data-pipeline/
│
├── data/
│ └── weather_data.csv # Original input file
│
├── outputs/
│ ├── transformed_weather_data.csv # Cleaned & transformed weather data
│ ├── temperature_report.txt # (Optional) Top 5 hottest cities
│ └── avg_temp_bar_chart.png # (Optional) Bar chart of avg temperatures
│
├── weather_pipeline.py # Main Python script
├── requirements.txt # Python dependencies
└── README.md # This file

