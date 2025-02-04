import sqlite3
from tabulate import tabulate

# Establish a connection to the SQLite database
conn = sqlite3.connect('Disease.db')
cursor = conn.cursor()

def create_table_diabetes():
    """
    Create a table named 'tabDiabetes' in the SQLite database.
    The table has fields for storing diabetes data.
    """
    sql_command = """CREATE TABLE IF NOT EXISTS tabDiabetes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    no_of_pregnancies DECIMAL(7,2),
    glucose_level DECIMAL(7,2),
    blood_pressure_value DECIMAL(7,2),
    skin_thickness DECIMAL(7,2),
    insulin_level DECIMAL(7,2),
    BMI DECIMAL(7,2),
    diabetes_pedigree DECIMAL(7,2),
    age DECIMAL(7,2),
    Result VARCHAR(100)
);
"""
    cursor.execute(sql_command)
    print("Table 'tabDiabetes' created...")


def create_table_heart():
    """
    Create a table named 'tabHeart' in the SQLite database.
    The table has fields for storing heart disease data.
    """
    sql_command = """CREATE TABLE IF NOT EXISTS tabHeart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    sex VARCHAR(10),
    chestpain DECIMAL(7,2),
    bp DECIMAL(7,2),
    cholestoral DECIMAL(7,2),
    BS DECIMAL(7,2),
    EleCardo DECIMAL(7,2),
    HR DECIMAL(7,2),
    EIA DECIMAL(7,2),
    Depression DECIMAL(7,2),
    ST DECIMAL(7,2),
    flouroscopy DECIMAL(7,2),
    thal DECIMAL(7,2),
    Result VARCHAR(100)
);
"""
    cursor.execute(sql_command)
    print("Table 'tabHeart' created...")


def create_table_parkinson():
    """
    Create a table named 'tabPark' in the SQLite database.
    The table has fields for storing Parkinson's disease data.
    """
    sql_command = """CREATE TABLE IF NOT EXISTS tabPark (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fo DECIMAL(7,2),
    fhi DECIMAL(7,2),
    flo DECIMAL(7,2),
    Jitter_percent DECIMAL(7,2),
    Jitter_Abs DECIMAL(7,2),
    RAP DECIMAL(7,2),
    PPQ DECIMAL(7,2),
    DDP DECIMAL(7,2),
    Shimmer DECIMAL(7,2),
    Shimmer_dB DECIMAL(7,2),
    APQ3 DECIMAL(7,2),
    APQ5 DECIMAL(7,2),
    APQ DECIMAL(7,2),
    DDA DECIMAL(7,2),
    NHR DECIMAL(7,2),
    HNR DECIMAL(7,2),
    RPDE DECIMAL(7,2),
    DFA DECIMAL(7,2),
    spread1 DECIMAL(7,2),
    spread2 DECIMAL(7,2),
    D2 DECIMAL(7,2),
    PPE DECIMAL(7,2),
    Result VARCHAR(100)
);
"""
    cursor.execute(sql_command)
    print("Table 'tabPark' created...")


def add_value_diabetes(no_of_pregnancies, glucose_level, blood_pressure_value, skin_thickness, insulin_level, BMI, diabetes_pedigree, age, result):
    """
    Add a new row to the 'tabDiabetes' table in the SQLite database.
    The row contains diabetes data.
    """
    try:
        cursor.execute("""
            INSERT INTO tabDiabetes 
            (no_of_pregnancies, glucose_level, blood_pressure_value, skin_thickness, insulin_level, BMI, diabetes_pedigree, age, Result) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (no_of_pregnancies, glucose_level, blood_pressure_value, skin_thickness, insulin_level, BMI, diabetes_pedigree, age, result))
        print("Added successfully to 'tabDiabetes'!")
        conn.commit()
    except sqlite3.Error as e:
        print("Error:", e)


def add_value_heart(age, sex, chestpain, bp, cholestoral, BS, EleCardo, HR, EIA, Depression, ST, flouroscopy, thal, result):
    """
    Add a new row to the 'tabHeart' table in the SQLite database.
    """
    try:
        cursor.execute("""
            INSERT INTO tabHeart 
            (age, sex, chestpain, bp, cholestoral, BS, EleCardo, HR, EIA, Depression, ST, flouroscopy, thal, Result) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (age, sex, chestpain, bp, cholestoral, BS, EleCardo, HR, EIA, Depression, ST, flouroscopy, thal, result))
        print("Added successfully to 'tabHeart'!")
        conn.commit()
    except sqlite3.Error as e:
        print("Error:", e)


def add_value_parkinson(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE, result):
    """
    Add a new row to the 'tabPark' table in the SQLite database.
    """
    try:
        cursor.execute("""
            INSERT INTO tabPark 
            (fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE, Result) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE, result))
        print("Added successfully to 'tabPark'!")
        conn.commit()
    except sqlite3.Error as e:
        print("Error:", e)


def fetch_and_print_data(table_name):
    """
    Fetch and print all data from the specified table in a tabular format.
    """
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        headers = [description[0] for description in cursor.description]
        print(f"\nData from {table_name}:")
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
    except sqlite3.Error as e:
        print("Error:", e)


# Create tables if they don't exist
"""create_table_diabetes()
create_table_heart()
create_table_parkinson()"""

# Example usage:
# add_value_diabetes(2, 120, 80, 25, 30, 25, 0.5, 40, 'Positive')
# add_value_heart(45, 'Male', 1, 120, 200, 120, 1, 0.8, 70, 1, 0.6, 1, 2, 'Positive')
# add_value_parkinson(150, 200, 100, 0.5, 0.02, 0.2, 0.3, 0.5, 0.02, 0.1, 0.2, 0.3, 0.4, 0.02, 0.1, 0.8, 0.6, 0.7, 0.5, 0.3, 0.2, 0.8, 'Positive')

# Fetch and print data from each table
fetch_and_print_data("tabDiabetes")
fetch_and_print_data("tabHeart")
fetch_and_print_data("tabPark")

# Close the connection
conn.close()
