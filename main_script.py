import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Data Ingestion
df = pd.read_csv("data/weather_data.csv")
# Replace NaNs in temperature, humidity, and wind speed with the city-wise mean
cols = ['temperature_celsius', 'humidity_percent', 'wind_speed_kph']
for col in cols:
    df[col] = df[col].fillna(df.groupby('city')[col].transform('mean'))

# Drop rows with NaN in date
df = df.dropna(subset=['date'])

# Standardize dates
df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce')

# Convert temperature to Fahrenheit
df["temperature_fahrenheit"] = (df["temperature_celsius"] * 9 / 5) + 32

# Filter rows where weather_condition is not 'Unknown' or null
df_filtered = df[(df['weather_condition'].notna()) & (df['weather_condition'] != 'Unknown')]

# Save cleaned and transformed data to CSV
df_filtered.to_csv("outputs/tranformed_weather_data.csv", index=False)

# Bonus: Generate a simple report of top 5 cities by average temperature_celsius
avg_temp_by_city = df_filtered.groupby("city")["temperature_celsius"].mean().sort_values(ascending=False).head(5)

# Save report as Markdown
report_path = "outputs/top_5_hottest_cities.md"
with open(report_path, "w") as report_file:
    report_file.write("# Top 5 Hottest Cities by Average Temperature (°C)\n\n")
    for city, temp in avg_temp_by_city.items():
        report_file.write(f"- **{city}**: {temp:.2f} °C\n")

# A bar chart of average temperature per city using matplotlib
df_filtered.groupby("city")["temperature_celsius"].mean().plot(kind ="bar")
plt.title("Average Temperature per City")
plt.xlabel("Cities")
plt.xticks(rotation=0)
plt.ylabel("Average Tempearture")
plt.savefig("outputs/avg_temp_bar_chart.png")
plt.show()

print("Transformation complete. Output files are saved in the 'outputs' directory.")
