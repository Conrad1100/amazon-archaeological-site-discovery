import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns

# Load the coordinates
df = pd.read_csv('anomaly_coordinates.csv')

# Standardize column names (if needed)
df.columns = df.columns.str.lower()

# Extract coordinates
coords = df[['longitude', 'latitude']].values

# Run DBSCAN clustering
db = DBSCAN(eps=0.01, min_samples=15).fit(coords)
df['cluster'] = db.labels_

# Count clusters
num_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
print(f"✅ Number of clusters found: {num_clusters}")

# Save clustered points
df.to_csv("clustered_anomalies.csv", index=False)

# Plot results
plt.figure(figsize=(10, 8))
sns.scatterplot(x='longitude', y='latitude', hue='cluster', palette='tab10', data=df, s=15)
plt.title('Clustered Anomalies (DBSCAN)')
plt.legend(title="Cluster ID", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("clustered_anomalies.png")
plt.show()
