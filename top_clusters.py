import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load clustered data
df = pd.read_csv('clustered_anomalies.csv')

# Exclude noise points (cluster -1)
df = df[df['cluster'] != -1]

# Count points per cluster
cluster_counts = df['cluster'].value_counts().reset_index()
cluster_counts.columns = ['cluster', 'count']

# Show top 5 clusters
print("\n🏆 Top 5 Clusters by Anomaly Count:")
print(cluster_counts.head())

# Filter top clusters (adjust number if needed)
top_clusters = cluster_counts.head(5)['cluster'].tolist()
top_df = df[df['cluster'].isin(top_clusters)]

# Save for mapping
top_df.to_csv("top_clusters.csv", index=False)



plt.figure(figsize=(10, 8))
sns.scatterplot(data=top_df, x='longitude', y='latitude', hue='cluster', palette='Set2', s=20)
plt.title('Top 5 Clusters of Potential Sites')
plt.legend(title='Cluster ID', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("top_5_clusters.png")
plt.show()
