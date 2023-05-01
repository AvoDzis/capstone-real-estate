# Real-Estate House Pricing Analysis for Yerevan Armenia
The purpose of this project is to analyze the Yerevan real estate market and provide insights into its trends, prices, and demand for different types of properties. Before we dive into the details of our analysis, we would like to acknowledge GeoVibe for providing us with the data that we used for this research. The data was collected by scraping three prominent real estate websites - list.am, estate.am, and real-estate.am. The extracted information such as ID, price, square meters, height, and other relevant details from each website using web scraping techniques. Arc-GIS is the main tool used to for the analysis regarding the prediction models. The following models were used

- Generalized Linear Regression
- Geographically Weighted Regression
- Forest Based Classigfication & Regressions

All of these models are native to ArcGIS, and the explanation of how each of these models work is outlined in the paper.Furthermore, you can find more information regarding how each of these models were modified to better fit the context of the data for Armenia, in the paper. It is important to mention as well that we have two versions of the raw data initially.

1. **Yerevan historical:** which includes the data that has been being scraped over time, but has disappeared from lisitings thus being classified as a house that was 'sold'
2. **Yerevan actual:** which includes the data with houses that were up to March 13th 2023 listed as active and ready to be sold.

You can find these files the under Database/raw_data folder.

In the paper, we have provided a comprehensive overview of the project, including the research objectives, the methodology used, and the results obtained. We have also included details of our data cleaning and preprocessing techniques, as well as information on how we generated the additional features using Arc-GIS, Google Maps API, and the Nominatim package. Our project will be of interest to anyone looking to gain insights into the Yerevan real estate market, and we hope that it will be a useful resource for researchers, policymakers, and other stakeholders.

## Folders
There are three main folders for this project.

1. **code:** This folder contains the code used for the project. The code includes Python scripts for data cleaning, data preparation, feature engineering, and  analysis of the model results.

2. **database:** This folder contains the raw data provided by GeoVibe, as well as the processed data that was used for model building and analysis.

3. **arc_gis_project:** This folder contains the ArcGIS project files, which include the maps, layers, and models that were built for this project.

You can find more information regarding each file if you click on the folders and review the README file there
