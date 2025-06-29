# generate_cluster_outlines.py (simplified snippet)
import geopandas as gpd
import matplotlib.pyplot as plt

# Load cluster GeoJSONs
gdf = gpd.read_file("data/cluster_outlines.geojson")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
gdf.boundary.plot(ax=ax, edgecolor='red', linewidth=2)
gdf.plot(ax=ax, alpha=0.3)
gdf['density'] = gdf.area / gdf.area.max()  # dummy density if not already computed
gdf.apply(lambda row: ax.annotate(
    f"#{row.name}", xy=(row.geometry.centroid.x, row.geometry.centroid.y),
    ha='center', fontsize=9), axis=1)

plt.title("🧭 Cluster Outlines with Density Annotations")
output_path = "data/cluster_outline_density_map.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✅ Saved: {output_path}")
