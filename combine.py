import numpy as np
import rasterio
from rasterio.enums import Resampling
from rasterio.warp import reproject, calculate_default_transform

# --- Load NDVI anomaly mask ---
with rasterio.open('data/ndvi_anomaly_mask.tif') as ndvi_src:
    ndvi_anomalies = ndvi_src.read(1)
    ndvi_meta = ndvi_src.meta.copy()

# --- Load elevation-based earthwork mask ---
with rasterio.open('data/elevated_flat_mask.tif') as elev_src:
    flat_elevated = elev_src.read(1)
    elev_meta = elev_src.meta.copy()

    # Prepare output array and transform
    reprojected = np.empty_like(ndvi_anomalies)

    reproject(
        source=flat_elevated,
        destination=reprojected,
        src_transform=elev_meta['transform'],
        src_crs=elev_meta['crs'],
        dst_transform=ndvi_meta['transform'],
        dst_crs=ndvi_meta['crs'],
        resampling=Resampling.nearest
    )

# --- Combine aligned masks ---
potential_sites = (ndvi_anomalies & reprojected).astype(np.uint8)

# --- Save combined mask ---
output_path = 'data/potential_sites_mask.tif'
with rasterio.open(
    output_path, 'w',
    driver='GTiff',
    height=potential_sites.shape[0],
    width=potential_sites.shape[1],
    count=1,
    dtype=rasterio.uint8,
    crs=ndvi_meta['crs'],
    transform=ndvi_meta['transform']
) as dst:
    dst.write(potential_sites, 1)

print(f"✅ Combined mask saved: {output_path}")

