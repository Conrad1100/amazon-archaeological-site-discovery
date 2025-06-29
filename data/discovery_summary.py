import os
import geopandas as gpd

# Get absolute path to the current script directory
base_dir = os.path.dirname(__file__)
geojson_path = os.path.join(base_dir, "new_discovery_candidates.geojson")

# Debug: Print full path to confirm it's correct
print("📁 Looking for:", geojson_path)

# Load the GeoJSON file
gdf = gpd.read_file(geojson_path)

# Print summary
print("\n🏆 Summary of New Discovery Candidates")
print("📊 Total Candidates:", len(gdf))

# Print first few rows (just coordinates)
print("\n📍 Sample Locations:")
print(gdf[['geometry']].head())

# Optional: Bounding box of discoveries
print("\n🗺️ Bounding Box:")
print(gdf.total_bounds)  # [minx, miny, maxx, maxy]
