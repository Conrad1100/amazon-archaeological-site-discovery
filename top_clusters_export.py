import os
import geopandas as gpd
from shapely.geometry import Point

from top_clusters import top_df, top_clusters

# Make sure output directory exists
os.makedirs("data/geojson", exist_ok=True)

# Convert to GeoDataFrame
geometry = [Point(xy) for xy in zip(top_df.longitude, top_df.latitude)]
gdf = gpd.GeoDataFrame(top_df, geometry=geometry)
gdf.set_crs(epsg=4326, inplace=True)

# Save each cluster to separate GeoJSONs
for cluster_id in top_clusters:
    cluster_gdf = gdf[gdf['cluster'] == cluster_id]
    out_path = f"data/geojson/cluster_{cluster_id}.geojson"
    cluster_gdf.to_file(out_path, driver="GeoJSON")
    print(f"📦 Saved: {out_path}")
