import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Load the anomaly coordinates CSV
df = pd.read_csv("anomaly_coordinates.csv")

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=[Point(lon, lat) for lon, lat in zip(df['Longitude'], df['Latitude'])],
    crs="EPSG:4326"
)

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, markersize=2, color="red", alpha=0.5)
ax.set_title("Mapped Anomalies in the Amazon Region")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("static_anomaly_map.png")
plt.show()
