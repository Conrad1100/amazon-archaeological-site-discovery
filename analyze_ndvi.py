import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Step 1: Load NDVI GeoTIFF ---
ndvi_path = "ndvi_sao_felix.tif"  # Update if saved elsewhere

if not os.path.exists(ndvi_path):
    raise FileNotFoundError(f"NDVI file not found at: {ndvi_path}")

with rasterio.open(ndvi_path) as src:
    ndvi = src.read(1)
    ndvi_meta = src.meta

# --- Step 2: Mask Invalid Data ---
ndvi = np.where((ndvi < -1.0) | (ndvi > 1.0), np.nan, ndvi)

# --- Step 3: Visualize NDVI ---
plt.figure(figsize=(10, 6))
plt.title("NDVI Map - São Félix do Araguaia")
ndvi_plot = plt.imshow(ndvi, cmap='YlGn', vmin=-1, vmax=1)
plt.colorbar(ndvi_plot, label="NDVI Value")
plt.axis('off')
plt.tight_layout()
plt.show()

# --- Step 4: Highlight Low-Vegetation Areas (Possible Anomalies) ---
low_ndvi_mask = ndvi < 0.3  # Customize threshold if needed

plt.figure(figsize=(10, 6))
plt.title("Low Vegetation Zones (NDVI < 0.3)")
plt.imshow(low_ndvi_mask, cmap='Reds')
plt.axis('off')
plt.tight_layout()
plt.show()

