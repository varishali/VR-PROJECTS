import pandas as pd
from src.data_loader import load_and_inspect_data
from src.data_cleaner import clean_data
from src.sql_query import run_sql_query
from src.visualization import generate_visualization

# terminal setting
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 1000)

def main():
    # paths setup 
    data_path = 'Titanic Projects/data/train.csv'
    chart_output_path = 'Titanic Projects/titanic_analysis_chart.png'

    # Step1: Load
    df = load_and_inspect_data(data_path)

    # Step2: Clean
    cleaned_df = clean_data(df)

    # Step3: SQL Analysis
    run_sql_query(cleaned_df)

    # Step4: Data Visualysis
    generate_visualization(cleaned_df, chart_output_path)

if __name__ == "__main__":
    main()
