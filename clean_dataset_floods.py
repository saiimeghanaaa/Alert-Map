import pandas as pd

# Load weather dataset
df = pd.read_csv("weather_dataset_19-01-2020.csv")

print("🔎 First 5 rows:")
print(df.head())

print("\n📊 Columns in dataset:")
print(df.columns)

# --- Step 1: Keep only useful columns ---
useful_cols = [
    "country",
    "index_date_format",  # date column
    "temparature",        # temperature
    "wind_direction",     # wind direction
    "sky",                # sky condition
    "pressure",           # pressure
    "location",           # location text
    "place"               # station/place
]
df = df[useful_cols]

# --- Step 2: Convert date ---
df["index_date_format"] = pd.to_datetime(df["index_date_format"], errors="coerce")

# --- Step 3: Handle missing values ---
df = df.dropna(subset=["country", "index_date_format"])  # require country & date

# --- Step 4: Optional renaming for clarity ---
df = df.rename(columns={
    "index_date_format": "date",
    "temparature": "temperature",
    "wind_direction": "wind_direction",
    "pressure": "pressure"
})

# --- Step 5: Save cleaned dataset ---
df.to_csv("weather_global_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as weather_global_cleaned.csv")