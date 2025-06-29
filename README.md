HEAD
 Amazon Archaeological Site Discovery  

An AI-powered exploration of the Amazon Rainforest using open-source geospatial and remote sensing data to uncover previously undocumented archaeological site candidates.

Overview 

This project was created for the [OpenAI to Z Challenge on Kaggle](https://www.kaggle.com/competitions/openai-to-z-challenge). It combines high-resolution satellite imagery, NDVI anomaly analysis, elevation filtering, and clustering techniques to identify potential ancient settlements hidden under the Amazon canopy. All discoveries were done using OpenAI tools. 

Objective 

To predict and present compelling evidence of new archaeological site candidates within the Amazon biome, with a primary focus on Brazil and neighboring countries.

Methodology Summary 

1. Data Sources:

   * Sentinel-2 imagery (NDVI analysis)
   * NASA SRTM Elevation data
   * Known archaeological site locations
   * OpenTopography & published LiDAR references

2. Pipeline:

   * NDVI anomaly detection
   * Elevation filtering to detect flat terrain
   * DBSCAN clustering of overlapping anomalies
   * Area filtering and ranking of site candidates
   * Verification against known archaeological maps

3. Visual Outputs: 

   * NDVI anomaly basemap overlay
   * Elevation slope mask
   * Clustering map with convex outlines
   * Summary plots and CSV/GeoJSON exports
   * Optional animated evolution from raw tiles to final clusters

Use of OpenAI Tools 

* ChatGPT (o4): Iterative research planning, and code troubleshooting.
* GPT-4.1 / o3: Geospatial algorithm ideation and visual narrative building  

Results 

*Top 5 Candidates discovered with significant NDVI anomalies, flat terrain, and density clustering 
* GeoJSON outputs and centroid-located summaries exported
* Visual confirmations and overlays provided

 Sample Discoveries 

All candidate sites are visualized in `data/discovery_map.html` and `data/cluster_outlines.geojson`, with supplementary maps included as PNGs in the repo.

Reproducibility 

The entire pipeline can be rerun using the included Python scripts. Key scripts include:

* `analyze_ndvi.py`
* `detect_flat_elevation.py`
* `DBSCAN_Clustering.py`
* `generate_cluster_outlines.py`
* `compare_with_known_sites.py`
* `generate_report_word.py`

References and Citations 

* [Kuhikugu Pre-Columbian Complex (DOI:10.1126/science.1184723)](https://doi.org/10.1126/science.1184723)
* Sentinel-2 Scenes: `S2B_MSIL2A_20250421T135759_N0509_R024_T22LEC_20250421T153307`
* Elevation data: NASA SRTM

License 

This project is open-sourced under the MIT License.

 Folder Structure (Flat Layout for Compatibility) 

```
.
├── analyze_ndvi.py
├── cluster_summary.csv
├── data/
│   ├── cluster_outlines.geojson
│   ├── discovery_map.html
│   ├── known_archaeo_sites.geojson
│   └── ...
├── generate_cluster_outlines.py
├── highlight_ndvi_anomalities.py
├── generate_report_word.py
└── ...
```

 
=======
ECHO is on.
>>>>>>> d28dda3 (Add full project files and updated README)
