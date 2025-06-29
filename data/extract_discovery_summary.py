import geopandas as gpd

# Load GeoJSON
gdf = gpd.read_file(r"C:\Users\Hp\PycharmProjects\pythonProject2\new_discovery_candidates.geojson")

# Reproject to metric CRS for accurate area (if not already done)
gdf = gdf.to_crs(epsg=3857)
gdf["area_sqkm"] = gdf.geometry.area / 1e6

# Back to geographic CRS for centroids
gdf = gdf.to_crs(epsg=4326)
gdf["centroid_lat"] = gdf.geometry.centroid.y
gdf["centroid_lon"] = gdf.geometry.centroid.x

# Select and export
summary_df = gdf[["area_sqkm", "centroid_lat", "centroid_lon"]]
summary_df.to_csv("data/discovery_candidates_summary.csv", index=False)

print("📄 Summary exported to: data/discovery_candidates_summary.csv")
