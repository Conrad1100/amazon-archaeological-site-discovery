import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import contextily as ctx

# Load anomaly CSV
df = pd.read_csv("anomaly_coordinates.csv")

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=[Point(lon, lat) for lon, lat in zip(df["Longitude"], df["Latitude"])],
    crs="EPSG:4326"  # WGS84
)

# Reproject to Web Mercator for basemap
gdf = gdf.to_crs(epsg=3857)

# Plot with basemap
fig, ax = plt.subplots(figsize=(12, 10))
gdf.plot(ax=ax, markersize=3, color="red", alpha=0.6, label="Anomalies")

# Add basemap tiles
ctx.add_basemap(ax, source=ctx.providers.Esri.WorldImagery)
ax.set_title("Anomalies Overlaid on Satellite Map")
ax.legend()
plt.tight_layout()
plt.savefig("anomalies_basemap_overlay.png")
plt.show()
