import pandas as pd

# Load merged file
df = pd.read_csv("fires_global_2024.csv")

print("🔎 First 5 rows:")
print(df.head())

print("\n📊 Columns in dataset:")
print(df.columns)

# --- Step 1: Keep only useful columns ---
# (adjust this list based on your dataset's columns)
useful_cols = ["latitude", "longitude", "acq_date", "acq_time", "brightness", "confidence", "country"]
df = df[useful_cols]

# --- Step 2: Convert date ---
df["acq_date"] = pd.to_datetime(df["acq_date"], errors="coerce")

# --- Step 3: Handle missing values ---
df = df.dropna(subset=["latitude", "longitude", "acq_date"])  # drop rows missing important data

# --- Step 4: Save cleaned file ---
df.to_csv("fires_global_2024_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as fires_global_2024_cleaned.csv")
