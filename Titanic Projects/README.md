# Titanic Data Analysis Pipeline (Modular Architecture)

This is an end-to-end Data Analysis project on the Titanic dataset, built using a **Modular Python Architecture**. The project is split into separate modules for data loading, cleaning, SQL queries, and visualization for better scalability and clean code standards.

---

## Project Structure

```text
Titanic Projects/
│
├── data/
│   └── train.csv                # Raw Titanic Dataset
│
├── src/
│   ├── data_loader.py           # Loads CSV & inspects basic info
│   ├── data_cleaner.py          # Handles missing values & drops unwanted columns
│   ├── sql_query.py             # SQLite integration & SQL analytical queries
│   └── visualization.py         # Matplotlib & Seaborn visualizations
│
├── main.py                      # Main pipeline execution script
├── titanic_analysis_chart.png   # Saved chart output
├── .gitignore                   # Ignores unwanted cache files
└── README.md                    # Project documentation