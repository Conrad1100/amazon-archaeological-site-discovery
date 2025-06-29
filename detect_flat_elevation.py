import rasterio
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# Load elevation data
with rasterio.open('Amazon_Elevation.tif') as src:
    elevation = src.read(1)
    transform = src.transform
    res = src.res[0]  # pixel size in meters

# --- 1. Compute Slope ---
# Use Sobel filter to approximate gradient
dzdx = ndimage.sobel(elevation, axis=1) / (8 * res)
dzdy = ndimage.sobel(elevation, axis=0) / (8 * res)
slope = np.sqrt(dzdx**2 + dzdy**2)

# --- 2. Threshold Slope (flat areas) ---
slope_threshold = 0.01  # adjust for sensitivity
flat_mask = slope < slope_threshold

# --- 3. Elevation Threshold (elevated land) ---
elevation_threshold = np.percentile(elevation[flat_mask], 75)
elevated_flat = flat_mask & (elevation > elevation_threshold)

# --- 4. Plot results ---
plt.figure(figsize=(10, 6))
plt.imshow(elevation, cmap='terrain', alpha=0.7)
plt.imshow(elevated_flat, cmap='autumn', alpha=0.5)
plt.title('Detected Flat Elevated Areas (Possible Earthworks)')
plt.colorbar(label='Elevation')
plt.axis('off')
plt.tight_layout()
plt.show()

# Optional: Save the binary mask for future analysis
np.save('data/earthwork_mask.npy', elevated_flat)
