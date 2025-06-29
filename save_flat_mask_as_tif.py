import numpy as np
import rasterio
from rasterio.transform import from_origin

# Load the elevation anomaly mask
flat_mask = np.load('data/earthwork_mask.npy')

# Define dummy transform (replace with real one from your elevation data if available)
transform = from_origin(-53.5, -11.0, 0.0001, 0.0001)  # adjust if needed

# Save as GeoTIFF
with rasterio.open(
    'data/elevated_flat_mask.tif',
    'w',
    driver='GTiff',
    height=flat_mask.shape[0],
    width=flat_mask.shape[1],
    count=1,
    dtype=rasterio.uint8,
    crs='EPSG:4326',
    transform=transform
) as dst:
    dst.write(flat_mask.astype(rasterio.uint8), 1)

print("✅ Saved elevation mask as: data/elevated_flat_mask.tif")

