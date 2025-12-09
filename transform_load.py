import pandas as pd
import sqlite3

# ===============================
# STEP 1 — Read Raw Data (Extract Output)
# ===============================

def load_raw_data():
    print("Reading raw Pokémon data...")
    df = pd.read_csv("raw_pokemon.csv")
    print("Raw data loaded successfully!")
    print(df.head())  # Show first 5 rows
    return df

# ===============================
# STEP 2 — Transform Data
# ===============================

def transform_data(df):
    print("Transforming data...")

    # Example Transformations
    df = df.copy()

    # Rename columns (optional but cleaner)
    df.rename(columns={
        "id": "pokemon_id",
        "name": "pokemon_name"
    }, inplace=True)

    print("Data after transformation:")
    print(df.head())

    return df

# ===============================
# STEP 3 — Load Data into SQLite (Star Schema)
# ===============================

def load_to_db(df):
    print("Loading data into SQLite database...")

    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()

    # Create Dimension Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_pokemon (
            pokemon_id INTEGER PRIMARY KEY,
            pokemon_name TEXT
        );
    """)

    # Create Fact Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_pokemon_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pokemon_id INTEGER,
            base_experience INTEGER,
            height INTEGER,
            weight INTEGER,
            FOREIGN KEY (pokemon_id) REFERENCES dim_pokemon(pokemon_id)
        );
    """)

    # Prepare dimension and fact data
    dim_df = df[["pokemon_id", "pokemon_name"]].drop_duplicates()
    fact_df = df[["pokemon_id", "base_experience", "height", "weight"]]

    # Load into DB
    dim_df.to_sql("dim_pokemon", conn, if_exists="replace", index=False)
    fact_df.to_sql("fact_pokemon_stats", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    print("Data loaded into pokemon.db (dim_pokemon & fact_pokemon_stats)")

# ===============================
# MAIN PROGRAM
# ===============================

def main():
    raw_df = load_raw_data()
    transformed_df = transform_data(raw_df)
    load_to_db(transformed_df)   # <<< اهم سطر

if __name__ == "__main__":
    main()
