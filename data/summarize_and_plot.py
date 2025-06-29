import geopandas as gpd
import matplotlib.pyplot as plt
import os

# === Step 1: Load Data ===
gdf = gpd.read_file(r"C:\Users\Hp\PycharmProjects\pythonProject2\new_discovery_candidates.geojson")

# === Step 2: Reproject to Projected CRS for accurate area and centroids ===
# UTM Zone 22S (EPSG:32722) is appropriate for parts of Brazil (Sao Félix area)
gdf_proj = gdf.to_crs(epsg=32722)

# === Step 3: Calculate area and centroid coordinates ===
gdf_proj['area_sqkm'] = gdf_proj.geometry.area / 1e6
gdf_proj['centroid_lon'] = gdf_proj.geometry.centroid.to_crs(epsg=4326).x
gdf_proj['centroid_lat'] = gdf_proj.geometry.centroid.to_crs(epsg=4326).y

# === Step 4: Print Summary ===
print("📊 Candidate Summary:")
print(gdf_proj[['area_sqkm', 'centroid_lat', 'centroid_lon']])

# === Step 5: Plot Area Bar Chart ===
plt.figure(figsize=(10, 6))
plt.barh(range(len(gdf_proj)), gdf_proj['area_sqkm'], color='skyblue')
plt.yticks(range(len(gdf_proj)), [f"Site {i}" for i in range(len(gdf_proj))])
plt.xlabel("Area (sq. km)")
plt.title("🌍 Estimated Area of Top 5 Discovery Candidates")

# Ensure output directory exists
os.makedirs("data", exist_ok=True)

# Save plot
plt.tight_layout()
plt.savefig("data/discovery_candidates_summary.png", dpi=300)
print("✅ Summary image saved to: data/discovery_candidates_summary.png")
