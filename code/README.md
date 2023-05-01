# Documentation for the code
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
- Creating a new modified version of the data for later usage by combine_actual_historical.ipynb file
