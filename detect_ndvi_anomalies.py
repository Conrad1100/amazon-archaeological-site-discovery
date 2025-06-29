import numpy as np
import rasterio
import os

# --- Load NDVI image ---
ndvi_path = 'ndvi_sao_felix.tif'  # Update path if needed

if not os.path.exists(ndvi_path):
    raise FileNotFoundError(f"NDVI file not found at: {ndvi_path}")

with rasterio.open(ndvi_path) as src:
    ndvi = src.read(1)
    profile = src.profile

# --- Define NDVI anomaly threshold ---
# Adjust threshold based on domain knowledge or experimentation
threshold = 0.2  # You can fine-tune this

# --- Detect anomalies ---
anomaly_mask = (ndvi < threshold).astype(np.uint8)  # Mark areas below threshold

# --- Save anomaly mask as image and .npy ---
os.makedirs('data', exist_ok=True)

# Save as GeoTIFF
anomaly_tif_path = 'data/ndvi_anomaly_mask.tif'
with rasterio.open(
    anomaly_tif_path, 'w',
    driver='GTiff',
    height=anomaly_mask.shape[0],
    width=anomaly_mask.shape[1],
    count=1,
    dtype=rasterio.uint8,
    crs=profile['crs'],
    transform=profile['transform']
) as dst:
    dst.write(anomaly_mask, 1)

# Save as .npy for analysis
np.save('data/ndvi_anomaly_mask.npy', anomaly_mask)

print(f"✅ NDVI anomaly detection complete.\nSaved GeoTIFF: {anomaly_tif_path}\nSaved array: ndvi_anomaly_mask.npy")
