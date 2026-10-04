# Real-Estate Price Analysis & Prediction for Yerevan, Armenia

My BS in Data Science capstone at the American University of Armenia (spring 2023). It was a team project with Davit Nazlukhanyan, supervised by Pakrad Balabanian. The full write-up is [`research_paper.pdf`](research_paper.pdf).

**Question:** which spatial data science technique predicts apartment sale prices in Yerevan best, and how can the results be visualised and validated?

## What we did

1. **Cleaning and feature engineering (Python, Jupyter).** We started from listings scraped from list.am, estate.am and real-estate.am, from August 2022 to March 2023. We removed duplicates, then added features:
   - the district, by reverse geocoding with Nominatim
   - the nearest metro station (haversine distance)
   - the walking distance to that station (Google Maps Directions API)
   - the neighbourhood (Google Geocoding API)

   Outliers were removed per district with the IQR rule, and coordinates were jittered before mapping.
2. **Modelling (ArcGIS Pro).** We trained three regression models on listings that had disappeared from the sites (treated as "sold"):
   - Generalized Linear Regression (GLR): a baseline, plus per-district, per-neighbourhood and multivariate-clustering variants built in ModelBuilder
   - Geographically Weighted Regression (GWR)
   - Forest-based Classification and Regression (FBCR)

   Listings still active on 13 March 2023 served as validation data.
3. **Spatio-temporal analysis (ArcGIS Pro).** A Space-Time Cube of sales, emerging hot-spot analysis, and Moran's I spatial autocorrelation.
4. **Evaluation (Python).** We compared the models on MAE, RMSE, R² and residuals.

## Results

From `code/predicted_price_analysis.ipynb`, run on the CSVs in `database/predicted_data/`. Prices are in USD.

| Model | R² (training, "sold") | RMSE (training) | R² (validation, active listings) | RMSE (validation) |
|---|---|---|---|---|
| GLR (per neighbourhood) | 0.67 | 46,278 | 0.46 | 66,810 |
| GWR | 0.74 | 41,259 | 0.64 | 55,019 |
| FBCR | **0.92** | **22,734** | **0.75** | **45,632** |

FBCR was the most accurate. All three models do noticeably worse on the validation set than on the training data.

## Repo layout

| Folder | Contents |
|---|---|
| [`code/`](code) | `functions.py` helpers and the Jupyter notebooks for cleaning, combining and evaluating ([details](code/README.md)) |
| [`database/`](database) | Cleaned and model-output CSVs. The raw scraped data isn't included ([details](database/README.md)) |
| [`arc_gis_capstone/`](arc_gis_capstone) | The ArcGIS Pro project (`.aprx`), toolbox, Space-Time Cube and exported results ([details](arc_gis_capstone/README.md)) |
| `research_paper.pdf` | The capstone paper |

## Running it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook code/
```

- `predicted_price_analysis.ipynb` runs on the CSVs in `database/`.
- The cleaning notebooks need the raw GeoVibe data, which isn't included. They also need a Google Maps API key in a `maps_api.txt` file at the repo root (git-ignored). See [`code/README.md`](code/README.md).
- The ArcGIS part needs ArcGIS Pro (Windows, paid licence). It also needs the project geodatabase, which is too large for the repo; see [`arc_gis_capstone/README.md`](arc_gis_capstone/README.md).

## Limitations

- This is a student project, not a reusable pipeline. The cleaning notebooks read and write intermediate files, and some of those (e.g. `Yerevan.xlsx`, `sale_combined_neighborhood.csv`) aren't in the repo.
- "Sold" is a proxy: a listing that disappeared from the sites was counted as sold.
- The modelling lives in ArcGIS Pro, so it can't be reproduced without an ArcGIS licence.

## Data credit

The listing data was collected and provided by **GeoVibe**, who scraped list.am, estate.am and real-estate.am. The raw data isn't redistributed here. Only cleaned, derived and model-output data is included.
