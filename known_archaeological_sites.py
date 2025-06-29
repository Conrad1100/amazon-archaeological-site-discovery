import geopandas as gpd
import matplotlib.pyplot as plt

# Load cluster outlines
clusters = gpd.read_file("data/cluster_outlines.geojson")

# Load known archaeological points (replace with actual path)
known_sites = gpd.read_file("data/known_archaeo_sites.geojson")

# Plot both
fig, ax = plt.subplots(figsize=(10, 10))
clusters.plot(ax=ax, facecolor="none", edgecolor="red", linewidth=2, label="Detected Clusters")
known_sites.plot(ax=ax, color="blue", markersize=20, label="Known Sites")

plt.legend()
plt.title("Comparison of Detected Clusters and Known Archaeological Sites")
plt.tight_layout()
plt.savefig("data/cluster_validation.png")
plt.show()
