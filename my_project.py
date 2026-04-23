import pandas as pd

# Sample EV data (dummy)
data = {
    "year": [2020, 2021, 2022, 2023, 2024],
    "demand": [100, 150, 220, 300, 400]
}

df = pd.DataFrame(data)

print("EV Demand Data:")
print(df)

# Simple prediction logic
year = int(input("\nEnter future year to predict demand: "))

last_year = df["year"].iloc[-1]
last_demand = df["demand"].iloc[-1]

# basic growth assumption
growth_rate = 0.25

years_diff = year - last_year
predicted_demand = int(last_demand * ((1 + growth_rate) ** years_diff))

print(f"\nPredicted EV demand for {year}: {predicted_demand}")
