import rasterio
import numpy as np
import pandas as pd

# Load the combined potential site mask
mask_path = 'data/potential_sites_mask.tif'
with rasterio.open(mask_path) as src:
    mask = src.read(1)
    transform = src.transform

# Get row, col indices of detected anomalies (where pixel == 1)
rows, cols = np.where(mask == 1)

# Convert pixel indices to geographic coordinates
coords = [rasterio.transform.xy(transform, row, col) for row, col in zip(rows, cols)]
lons, lats = zip(*coords)

# Save to CSV
df = pd.DataFrame({'Longitude': lons, 'Latitude': lats})
df.to_csv('potential_sites_coordinates.csv', index=False)

print(f"✅ Extracted {len(df)} coordinates and saved to potential_sites_coordinates.csv")
