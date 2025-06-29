import geopandas as gpd
import matplotlib.pyplot as plt

# Load known archaeological sites
known_sites = gpd.read_file("data/known_archaeo_sites.geojson")

# Load detected cluster outlines
clusters = gpd.read_file("data/cluster_outlines.geojson")

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
clusters.boundary.plot(ax=ax, edgecolor='blue', linewidth=2, label='Detected Clusters')
known_sites.plot(ax=ax, color='red', markersize=60, label='Known Archaeological Sites')

plt.legend()
plt.title("Detected Clusters vs Known Archaeological Sites")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("data/detected_vs_known_sites.png", dpi=300)
plt.show()
