# Data

The listing data comes from **GeoVibe**. They scraped list.am, estate.am and real-estate.am between August 30, 2022 and March 13, 2023, and provided it to us for this capstone. Only the cleaned, derived and model-output files below are in this repo.

## raw_data (not included)
The cleaning notebooks start from two raw files that GeoVibe provided. They aren't redistributed here, and the `database/raw_data/` folder is git-ignored:
- `Yerevan actual.csv`: listings still active on March 13, 2023 (51,893 rows)
- `Yerevan historical.xlsx`: listings that had disappeared from the sites, treated as sold (729,498 rows)

## yerevan_actual_clean
This folder contains data that is a version of Yerevan actual.csv but has been preprocessed and cleaned
- Yerevan.csv: unecessary columns removed, new key features added such as district, closest metro, walking distance to metro
- sale_actual.csv: a version of Yerevan.csv, but with outliers removed, and coordinates spatially jittered

## yerevan_historical_clean
This folder contains data that is a version of Yerevan historical.csv but has been preprocessed and cleaned
- Yerevan_Historical_sales.csv: unecessary columns removed, new key features added such as district, closest metro, walking distance to metro
- sale_historical.csv: a version of Yerevan.csv, but with outliers removed, and coordinates spatially jittered

 ## yerevan_combined_clean
This folder contains data that is a version of sale_historical.csv and sale_actual.csv but is modified in the following way
- actual_not_sold.csv: neighborhood feature for houses added
- historical_sold.csv: neighborhood feature for houses added, houses that were wrongly classified as sold removed
This is the starting data that is used in ArcGIS to builds the models and conduct the analysis

## predicted_data
This folder contains data that is exported from ArcGIS, and it contains the data that has the results of the trained data models, and validation/test data results
- **new_home_prediction**: Folder contains results from the validation/test data for all the models
  - fbcr_new_prediction.csv: Price predictions by the model FBCR for the new data points (actual_not_sold.csv)
  - glr_new_prediction.csv: Price predictions by the model GLR for the new data points (actual_not_sold.csv)
  - gwr_new_prediction.csv: Price predictions by the model GWR for the new data points (actual_not_sold.csv)
- fbcr_predicted.csv: Price predictions by the FBCR model for trainning data (historical_sold.csv)
- glr_baseline_predicted.csv: Price predictions by the baseline GLR model for trainning data (historical_sold.csv)
- glr_district_predicted.csv: Price predictions by the district GLR for trainning data (historical_sold.csv)
- glr_improvement_results_table.csv: Contains the results of how much better the Neighborhood GLR performed in each neighborhood over the baseline GLR model 
- glr_multi_predicted.csv: Price predictions by the Multivariate Clustering GLR model for trainning data (historical_sold.csv)
- glr_predicted.csv: Price predictions by the Neighborhood GLR model for trainning data (historical_sold.csv)
- gwr_predicted.csv: Price predictions by the GWR model for trainning data (historical_sold.csv)


