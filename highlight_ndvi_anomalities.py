import numpy as np
import rasterio
import matplotlib.pyplot as plt

# --- Step 1: Load NDVI image ---
ndvi_path = "ndvi_sao_felix.tif"
with rasterio.open(ndvi_path) as src:
    ndvi = src.read(1)
    ndvi_meta = src.meta

# --- Step 2: Set NDVI threshold range ---
# Typical dense vegetation is > 0.5; values < 0.3 may indicate cleared areas or anomalies
vegetation_mask = ndvi > 0.5
anomalies_mask = (ndvi > 0.1) & (ndvi < 0.3)

# --- Step 3: Plot ---
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Raw NDVI")
plt.imshow(ndvi, cmap="YlGn")
plt.colorbar()

plt.subplot(1, 3, 2)
plt.title("Dense Vegetation (NDVI > 0.5)")
plt.imshow(vegetation_mask, cmap="Greens")

plt.subplot(1, 3, 3)
plt.title("Possible Anomalies (0.1 < NDVI < 0.3)")
plt.imshow(anomalies_mask, cmap="Oranges")

plt.tight_layout()
plt.show()
