import rasterio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LightSource
import matplotlib.cm as cm  # Fix: import color maps

# --- File path to your elevation GeoTIFF ---
elevation_path = 'Amazon_Elevation.tif'  # Update if needed

# --- Load elevation data ---
with rasterio.open(elevation_path) as src:
    elevation = src.read(1)
    transform = src.transform

# --- Create hillshade with proper colormap ---
ls = LightSource(azdeg=315, altdeg=45)
terrain_cmap = cm.get_cmap('terrain')  # Fix: get colormap object
hillshade = ls.shade(elevation, cmap=terrain_cmap, vert_exag=1, blend_mode='overlay')

# --- Plot hillshade elevation map ---
plt.figure(figsize=(10, 8))
plt.imshow(hillshade, extent=(0, elevation.shape[1], 0, elevation.shape[0]))
plt.title('Elevation with Hillshade Overlay')
plt.axis('off')
plt.colorbar(label='Elevation (m)', shrink=0.5)
plt.tight_layout()
plt.show()
