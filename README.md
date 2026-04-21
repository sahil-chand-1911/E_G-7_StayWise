# E_G-7_StayWise

This project provides an end-to-end data pipeline for analyzing key drivers of revenue and occupancy for Airbnb listings using Python and Jupyter Notebooks.

## Project Structure

- `notebooks/`:
    - `01_loading.ipynb`: Data ingestion and CSV parsing.
    - `02_cleaning.ipynb`: Data cleaning, handling missing values, and amenity processing.
    - `03_eda.ipynb`: Exploratory Data Analysis (distributions, correlations, market trends).
    - `04_statistical_analysis.ipynb`: Analysis of feature impacts (specifically amenities) on revenue.
    - `05_final_load_prep.ipynb`: Final data preparation and export for visualization.
- `scripts/`:
    - `etl_pipeline.py`: A Python script to automate the execution of all notebooks in order.
- `data/`:
    - `raw/`: Raw source files.
    - `processed/`: Intermediate processed files.
- `listings.csv`: Primary dataset containing listing details and TTM (Trailing Twelve Month) metrics.
- `past_rates.csv`: Historical rate and occupancy data.

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Pandas, Numpy, Matplotlib, Seaborn
- Jupyter Notebook / JupyterLab
- `nbconvert` (for running the ETL script)

### Running the Pipeline
You can run the entire pipeline from the root directory using:
```bash
python3 scripts/etl_pipeline.py
```
Alternatively, you can open and run the notebooks individually in the `notebooks/` folder.

## Key Features
- **Amenity Impact Analysis**: Identifies which amenities are most correlated with high revenue.
- **Market Segmentation**: Aggregates performance metrics by city and property type.
- **Data Robustness**: Handles parsing errors and standardizes categorical data across millions of rows.
