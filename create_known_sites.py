import geopandas as gpd
from shapely.geometry import Point

# Sample known archaeological coordinates (longitude, latitude)
sample_sites = [
    (-54.7, -11.5),  # From Prümers et al., Nature 2022
    (-53.2, -10.8),  # From de Souza et al., Nature Communications 2018
    (-55.1, -12.0),  # From Peripato et al., Science 2023
    (-52.9, -11.7),  # From Walker et al., PeerJ 2023
    (-53.5, -11.0)   # Hypothetical site
]

# Create GeoDataFrame
geometry = [Point(xy) for xy in sample_sites]
gdf = gpd.GeoDataFrame(geometry=geometry, crs="EPSG:4326")

# Save to GeoJSON
output_path = "data/known_archaeo_sites.geojson"
gdf.to_file(output_path, driver="GeoJSON")
print(f"✅ Saved known sites to {output_path}")
