import folium
import numpy as np
import rasterio
from rasterio.features import shapes
import geopandas as gpd
from shapely.geometry import shape

# Load the mask
mask_path = "data/potential_sites_mask.tif"
with rasterio.open(mask_path) as src:
    mask = src.read(1)
    transform = src.transform

# Extract geometries from mask
results = (
    {"properties": {"raster_val": v}, "geometry": s}
    for i, (s, v) in enumerate(shapes(mask, transform=transform)) if v == 1
)

# Convert to GeoDataFrame
geoms = list(results)
gdf = gpd.GeoDataFrame.from_features(geoms)

# Get center for map
center = gdf.geometry.unary_union.centroid
center_lat, center_lon = center.y, center.x

# Create the interactive map with terrain tiles and attribution
m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=10,
    tiles='https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
)

# Add each site as a polygon
for _, row in gdf.iterrows():
    sim_geo = gpd.GeoSeries([row['geometry']]).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    folium.GeoJson(data=geo_j, style_function=lambda x: {
        'fillColor': 'red', 'color': 'red', 'weight': 1, 'fillOpacity': 0.4
    }).add_to(m)

# Save the interactive map
m.save("potential_sites_map.html")
print("✅ Interactive map saved as: potential_sites_map.html")
