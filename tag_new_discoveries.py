import geopandas as gpd

# Load all clusters and intersecting clusters
all_clusters = gpd.read_file("data/cluster_outlines.geojson")
matched_clusters = gpd.read_file("data/matching_clusters.geojson")

# Find unmatched ones
unmatched_clusters = all_clusters[~all_clusters.geometry.isin(matched_clusters.geometry)]

# Tag and save
unmatched_clusters["status"] = "potential_discovery"
unmatched_clusters.to_file("data/new_discovery_candidates.geojson", driver="GeoJSON")

print(f"🌍 Saved {len(unmatched_clusters)} new discovery candidates to: data/new_discovery_candidates.geojson")
