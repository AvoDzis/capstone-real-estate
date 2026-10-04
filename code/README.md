# Documentation for the code

## Running the notebooks
- Run them from inside `code/`. They use relative paths like `../database/...`.
- `predicted_price_analysis.ipynb` runs on the CSVs in `database/predicted_data/` as-is.
- `yerevan_historical_cleaning.ipynb` and `yerevan_actual_cleaning.ipynb` need the raw GeoVibe files in `database/raw_data/`, which aren't included (see [database/README.md](../database/README.md)).
- The cleaning and combining notebooks call the Google Maps APIs (Directions and Geocoding). Put your own key in a file named `maps_api.txt` at the repo root. It's git-ignored, so the key never gets committed. These calls run once per listing, so they cost API quota.

## functions.py
This file includes the main functions that were imported to all of the files mentioned below:
- **get_district(lat, lng)**: Uses Nominatim package to reverse geocode the coordinates (lat, long) to get the district.
- **haversine(lon1, lat1, lon2, lat2)**: Calculate the great circle distance between two coordinate points on earth (specified in decimal degrees)
- **read_api_key()**: Reads the Google Maps API key from `maps_api.txt` in the parent of the current working directory (the repo root when you run from `code/`). The file is git-ignored, so the key stays out of the repo.
- **get_walking_distance(start_lon, start_lat, end_lon, end_lat)**: Calculate the walking distance between two points using the Google Maps API. Starting coordinate is each and every house in the data, the ending coordinate is the coordinate of their closest metro.
- **remove_outliers(df, col, lower_bound)**: Removes outliers from a dataframe based on the IQR method. Data is grouped by district, the outliers are detected for each district.
- **apply_jitter(coord, distance)**: Apply jittering to a coordinate (latitude and longitude).

## yerevan_historical_cleaning.ipynb & yerevan_actual_cleaning.ipynb
These two files can grouped together as they perform the same exact operations on the raw data for the hisorical houses that have been scraped (sold houses) and the actual houses (the houses that were still active untill March 13th 2023)
There are a few main things this section of the code does
- Drop unecessary columns
- Filter out duplicates id's
- Generate new valuable features for the table including:
  - The District each house belongs to
  - The Neighborhood each house belongs to
  - Their closest metro
  - Walking distance to the closest metro
- Outlier detection and elimination using IQR
- Creating a new modified versions of the data for later usage by combine_actual_historical.ipynb file

## combine_actual_historical.ipynb

This file acts as a way of connecting both of the new data's to each other, generating another column feature 'neighborhood' for later analysis. After the code here is run we will have two main files that will be used in ArcGIS.
- historical_sold.csv: the data here represent all of the houses that have been sold so far and will be used for the following main two reasons
  - Space-Time-Cube Analysis: Analysis of whether the sold houses locations match popular areas of the city, finding new hotspots
  - Training for Models: the data here will be used for training of the data for the models GLR, GWR, and FBCR in ArcGIS
- actual_not_sold.csv: this data will be used as validation/test data for the models that were trained with the historical data

## predicted_price_analysis.ipynb

After the data has been processed in ArcGIS, the specified models were trained on the historical data, and tested on the actual data, we have this file that aims to analyse the performance of each model. The following are the functionalities of this file.
- Compare the performance of the GLR model with it's different variations to find which one performs best on trained data
  - GLR using Multivariate Clustering
  - GLR grouped for each district
  - GLR grouped for each neighborhood (which performs the best)
- Compare how much better the GLR with neighborhoods performs better than the baseline approach of the GLR
- Reviewing diagnostics for the trained data for every model
- Reviewing diagnostics for the validation/test data for every model


