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
    - multi_cluster: Maps points of data for houses grouped by the clusters formed by the model
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

### Model Builder
This map also has the following ModelBuilders for the GLR prediction. You can see this looking at the catalog pane on the right...

1. 

## Map 2: Historical Data Analysis



## Map 3: Space-Time-Cube