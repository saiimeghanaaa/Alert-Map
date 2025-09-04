import pandas as pd

# Load the dataset
df = pd.read_csv(r'D:\1D 2D 3D G0!\Meteorite_Landings (3).csv')

# Step 1: Check GeoLocation format
print(df['GeoLocation'].head())  # Print a sample of the GeoLocation column

# Step 2: Extract 'reclat' and 'reclong' only if 'GeoLocation' has the correct format
# Using a try-except block for rows that may not match the expected format

def extract_lat_long(geolocation):
    try:
        # Extract values from the tuple format (lat, long)
        lat, long = geolocation.strip('()').split(', ')
        return float(lat), float(long)
    except:
        # Return None if the format is incorrect
        return None, None

# Apply the function to the GeoLocation column
df[['reclat', 'reclong']] = df['GeoLocation'].apply(lambda x: pd.Series(extract_lat_long(x)))

# Step 3: Display first few rows to verify
print(df[['name', 'GeoLocation', 'reclat', 'reclong']].head())

# Step 4: Check for missing values in reclat and reclong
print(df[['reclat', 'reclong']].isnull().sum())

# Step 5: Handle missing values (if needed)
# You can fill or drop rows with missing lat/long values as needed
# df = df.dropna(subset=['reclat', 'reclong'])  # Example: Drop rows with missing coordinates

# Step 6: Save the cleaned dataset
df.to_csv('cleaned_meteorites.csv', index=False)
