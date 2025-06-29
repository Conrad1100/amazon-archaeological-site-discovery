import geopandas as gpd

# Load GeoDataFrames
known_sites = gpd.read_file("data/known_archaeo_sites.geojson")
clusters = gpd.read_file("data/cluster_outlines.geojson")

# Set CRS to the same if not already
known_sites = known_sites.to_crs(epsg=4326)
clusters = clusters.to_crs(epsg=4326)

# Perform spatial join with buffer to allow near matches (~500 meters)
buffered_known = known_sites.buffer(0.005)  # ~500m buffer
buffered_known_gdf = gpd.GeoDataFrame(geometry=buffered_known, crs=known_sites.crs)

# Check intersection
intersections = clusters[clusters.intersects(buffered_known_gdf.unary_union)]

print(f"🔍 Clusters matching or near known sites: {len(intersections)} / {len(clusters)}")
intersections.to_file("data/matching_clusters.geojson", driver="GeoJSON")
