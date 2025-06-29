import imageio
import os

# Folder where your frames are saved
frame_dir = "data/animation_frames"
output_gif = "data/evolution_ndvi_to_clusters.gif"

# Collect all frame filenames in order
frames = sorted([
    os.path.join(frame_dir, f)
    for f in os.listdir(frame_dir)
    if f.endswith(".png")
])

# Create and save GIF
images = [imageio.imread(f) for f in frames]
imageio.mimsave(output_gif, images, fps=1)

print(f"✅ GIF saved to: {output_gif}")
