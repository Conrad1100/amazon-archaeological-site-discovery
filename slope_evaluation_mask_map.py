import geopandas as gpd
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# File paths
elevation_path = "Amazon_Elevation.tif"
combined_mask_path = "data/potential_sites_mask.tif"  # Slope + Elevation + NDVI
cluster_outlines_path = "data/cluster_outlines.geojson"
output_path = "data/slope_elevation_mask_map.png"

# Load raster and cluster outlines
elevation_src = rasterio.open(elevation_path)
mask_src = rasterio.open(combined_mask_path)
gdf = gpd.read_file(cluster_outlines_path)

# Create custom colormap for the mask (red highlights)
mask_cmap = ListedColormap(['none', 'red'])

# Plot everything
fig, ax = plt.subplots(figsize=(12, 10))

# Show elevation (grayscale hillshade effect)
show(elevation_src, ax=ax, cmap='Greys_r', alpha=0.8)

# Overlay combined mask
show(mask_src, ax=ax, cmap=mask_cmap, alpha=0.4)

# Optionally overlay cluster outlines
gdf.boundary.plot(ax=ax, edgecolor='blue', linewidth=1.5)

plt.title("🗻 Slope & Elevation Mask over Amazon Terrain", fontsize=14)
plt.axis('off')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✅ Map saved to: {output_path}")
