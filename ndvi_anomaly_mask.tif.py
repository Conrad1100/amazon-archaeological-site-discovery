import rasterio
import numpy as np

# Load your NDVI image (change path if needed)
ndvi_path = "ndvi_sao_felix.tif"
output_path = "data/ndvi_anomaly_mask.tif"

with rasterio.open(ndvi_path) as src:
    ndvi = src.read(1)
    profile = src.profile
    transform = src.transform

# Create anomaly mask (1 where 0.1 < NDVI < 0.3, else 0)
anomaly_mask = np.where((ndvi > 0.1) & (ndvi < 0.3), 1, 0).astype(np.uint8)

# Update profile to store mask as single-band 8-bit
profile.update(dtype=rasterio.uint8, count=1)

# Save the mask
with rasterio.open(output_path, "w", **profile) as dst:
    dst.write(anomaly_mask, 1)

print(f"✅ NDVI anomaly mask saved to {output_path}")
