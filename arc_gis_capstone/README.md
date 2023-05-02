# IMPOTANT!!!
Before you clone the repository visit this link: https://drive.google.com/file/d/1Uibbqcp2Xq46fyzTq61YVVT3_DaQ5YaW/view?usp=sharing

Load the folder arc_gis_capstone.gdb in this exact directory so you can have the geodatabse necessary for arcgis

# ArcGIS project outline

Once you have loaded the data and opened ArcGIS you will see that in ArcGIS you have maps that act as seperate project to load your data to and from there work on that project. You can see this in the Catalog pane on the right with folder called maps.
This project has three main maps that you will see in that Maps folder.

## Map 1: Models
In this map project you will find the data that was cleaned from the python code (review code section for more detaials)
We have the following structure of Folders in the maps contents pane, with each folder having the following layer.
- **House Points**
  - actual_not_sold: Maps points of data for houses that haven't been sold yet
  - historical_sold: Maps points of data for houses that have been sold
- **Generalized Linear Regression**
  - historical_sold_glr: results from the baseline GLR
  - districts_glr: results from the district GLR
  - neighborhoods_glr: results from the neighborhood GLR
  - **Multivariate Clustering**
    - historical_multi_cluster: Maps points of data for houses grouped by the clusters formed by the model
    - multi_cluster_glr: results from the Multivariate Clustering GLR
- **Geographically Weighted Regression**
  - historical_sold_sqmt_gwr: results from the GWR model
- **Local Bivariate Relationships**
  - local_rlns_height_sqmt: spatial relationship between variable height and square_meters for historical_sold data points
  - local_rlns_height_price: spatial relationship between variable height and price for historical_sold data points
  - local_rlns_height_sqmt: spatial relationship between variable square_meters and price for historical_sold data points
- **Forest Based Classification & Regression**
  - price_predicted_full: results from the baseline FBCR model
  - price_predicted: results from the Reduced FBCR model
  - price_predicted_reduced_hotspots: hotspot analysis for price prediction uncertainty
- **Comparison of Models**
  - comp_price1: predicted prices for validation/test data (actual_not_sold) grouped together
  - GLR Prediction: contains price prediction by the neighborhood GLR for validation/test data (actual_not_sold)
  - Forest Prediction: contains price prediction by the optimized FBCR for validation/test data (actual_not_sold)
  - GWR Prediction: contains price prediction by the GWR for validation/test data (actual_not_sold)

**Note**: The baseline GLR model, GWR model, baseline FBCR model, and Reduced FBCR model were all pyt together from the geoprocessing pane in ArcGIS, and you can find all of their details from the history pane on the right, by searching for each model. The modified GLR models were put together using the ModelBuilder tool in ArcGIS.

### Model Builder
This map also has the following ModelBuilders for the GLR prediction. You can see this looking at the catalog pane on the right by expanding the toolboxes folder.
1. **GLR by Districts**: GLR model that is trained based on each districts in Yerevan
2. **GLR by Neighborhood**: GLR model that is trained based on each neighborhood in Yerevan
3. **Multivariate Clustering GLR**: GLR model that is trained based on clusters of data points that was given by the Multivariate Clustering model
4. **New Homes Prediction GLR**: Uses the trained neighborhood GLR model to predict prices of new homes based on each neighborhood.

## Map 2: Historical Data Analysis
This Map contains 2D analysis of the houses that were sold (historical_sold.csv). It is mainly used to identify the ideal spots in real-estate investment, and finding locations of hotspots around the city that can be helpful for future businesses. In the contens pane you will find the following structure.
- historical_sold: Maps points of data for houses that have been sold
- sales_count: hexagon disivision of the map of Yerevan, to identify the hexagons that the most sales occur for
- sold_STC_2D: 2-dimensional Space-Time-Cube for the sales of houses on the Map of Yerevan.
- hot_spots: Contains the Emerging hotspot analysis for the space-time-cube hexagons, to identify, which hexagons are...
  - New Hot Spots
  - Persistent Hot Spots
  - Sporadic Hot Spots
  - No Pattern Detected
- DBSCAN: 
- ideal: 

## Map 3: Space-Time-Cube
This map contains 3D visual analysis of the spatiotemporal data for real-estate house sales in Yerevan.
- sold_STC_3D: 3D Space-Time-Cubes triggered on a tri-weekly basis, with each hexagon spanning 800m^2 of area. Space-Time-Cube was triggered based on the count for each hexagon, thus the darker the color of the hexagon, the more houses were sold in that hexagon over it's specified three weeks.
- hot_spots: Contains the Emerging hotspot analysis for the space-time-cube hexagons, to identify, which hexagons are...
  - New Hot Spots
  - Persistent Hot Spots
  - Sporadic Hot Spots
- sold_STC_hot_spo_SpatialJoin:  3D Space-Time-Cubes triggered on a tri-weekly basis, with each hexagon spanning 800m^2 of area. Space-Time-Cube was triggered based on the hot and cold spots for each hexagon, thus the darker the color of the hexagon, the more confident the model is that the hexagon is a hotspot.