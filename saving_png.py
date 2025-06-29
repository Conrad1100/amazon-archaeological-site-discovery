# Save multiple stages for animation
import matplotlib.pyplot as plt
import rasterio
import numpy as np
import os

steps = [
    ("Raw NDVI", "ndvi_sao_felix.tif"),
    ("NDVI Anomalies", "data/ndvi_anomaly_mask.tif"),
    ("Elevation Mask", "Amazon_Elevation.tif"),
    ("Cluster Labels", "data/cluster_labels.tif"),
    ("Cluster Outlines", "data/cluster_outline_density_map.png")
]

os.makedirs("data/animation_frames", exist_ok=True)

for i, (title, path) in enumerate(steps):
    if path.endswith(".png"):
        img = plt.imread(path)
        plt.imshow(img)
    else:
        with rasterio.open(path) as src:
            img = src.read(1)
            plt.imshow(img, cmap='viridis')

    plt.title(title)
    plt.axis("off")
    frame_path = f"data/animation_frames/step_{i:02d}.png"
    plt.savefig(frame_path, bbox_inches="tight", pad_inches=0)
    plt.close()
