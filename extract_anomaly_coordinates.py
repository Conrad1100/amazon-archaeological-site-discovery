import rasterio
import numpy as np
import pandas as pd

# --- Load NDVI anomaly mask ---
anomaly_path = "data/ndvi_anomaly_mask.tif"

with rasterio.open(anomaly_path) as src:
    anomaly_mask = src.read(1)
    transform = src.transform

# --- Find coordinates of anomaly pixels (0.1 < NDVI < 0.3) ---
rows, cols = np.where(anomaly_mask == 1)

# Vectorized coordinate extraction
xs, ys = rasterio.transform.xy(transform, rows, cols)

# Create DataFrame with extracted coordinates
df_coords = pd.DataFrame({'Longitude': xs, 'Latitude': ys})

# Optional: Sample every Nth point to reduce size (adjust step as needed)
df_sampled = df_coords.iloc[::1000]  # e.g., every 1000th point

# Save to CSV
df_sampled.to_csv("anomaly_coordinates.csv", index=False)
print(f"✅ Saved {len(df_sampled)} sampled anomaly coordinates to anomaly_coordinates.csv")
