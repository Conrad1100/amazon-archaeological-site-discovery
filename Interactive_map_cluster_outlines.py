import geopandas as gpd
import folium

# Load the new discoveries
gdf = gpd.read_file("new_discovery_candidates.geojson")

# Center map
center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
m = folium.Map(location=center, zoom_start=9, tiles="OpenStreetMap")

# Add polygons to map
for idx, row in gdf.iterrows():
    folium.GeoJson(
        row.geometry,
        name=f"Cluster {idx}",
        tooltip=f"Potential Site {idx}",
        style_function=lambda x: {"fillColor": "#ff7800", "color": "#ff7800", "weight": 2, "fillOpacity": 0.4}
    ).add_to(m)

# Save
m.save("data/discovery_map.html")
print("🗺️ Interactive map saved to: data/discovery_map.html")
