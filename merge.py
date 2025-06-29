import pandas as pd

# Load original + previous augmented dataset
df_all = pd.read_csv("clustered_tiles_augmented.csv")

# Load vegetation-only augmented data
df_veg = pd.read_csv("clustered_tiles_vegetation_augmented.csv")

# Merge them
df_combined = pd.concat([df_all, df_veg], ignore_index=True)

# Save combined dataset
df_combined.to_csv("clustered_tiles_final.csv", index=False)
print("✅ Combined dataset saved as clustered_tiles_final.csv")
