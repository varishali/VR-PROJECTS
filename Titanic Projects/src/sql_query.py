import sqlite3
import pandas as pd

def run_sql_query(df):
    """
    SQLite in-memory database me data load karke SQL queries run karta hai.
    """
    conn = sqlite3.connect(':memory:')
    df.to_sql('titanic', conn, index=False, if_exists='replace')

    # Query1 -- Gender wise Survived Rate
    q1 = """

    SELECT Sex,
        COUNT(*) AS Total_Passengers,
        SUM(Survived) AS Survived_Count,
        ROUND(AVG(Survived)*100, 2) AS Survived_Rate_Pct
    FROM titanic
    GROUP BY Sex;         
    """
    print("\n=== SQL QUERY1: GENDER-WISE SURVIVAL ===")
    print(pd.read_sql_query(q1, conn))

    # Query2 -- Class wise Survived Rate
    q2 = """
    SELECT Pclass,
        COUNT(*) AS Total_Passengers,
        SUM(Survived) AS Survived_Count,
        ROUND(AVG(Survived)*100, 2) AS Survived_Rate_Pct
    FROM titanic
    GROUP BY Pclass
    ORDER BY Pclass;    
    """
    print("\n=== SQL QUERY2: CLASS-WISE SURVIVAL ===")
    print(pd.read_sql_query(q2, conn))

