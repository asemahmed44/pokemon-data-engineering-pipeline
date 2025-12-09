import sqlite3
import pandas as pd

DB_PATH = "pokemon.db"

def run_query(sql, params=None):
    if params is None:
        params = ()

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, conn, params=params)
    conn.close()
    return df


def main():
    print("1) Top 10 Pokémon by base_experience")
    q1 = """
    SELECT
        d.pokemon_id,
        d.pokemon_name,
        f.base_experience,
        f.height,
        f.weight
    FROM fact_pokemon_stats f
    JOIN dim_pokemon d
        ON f.pokemon_id = d.pokemon_id
    ORDER BY f.base_experience DESC
    LIMIT 10;
    """
    df1 = run_query(q1)
    print(df1)
    print("-" * 60)

    print("2) Average height and weight of all Pokémon")
    q2 = """
    SELECT
        AVG(height) AS avg_height,
        AVG(weight) AS avg_weight
    FROM fact_pokemon_stats;
    """
    df2 = run_query(q2)
    print(df2)
    print("-" * 60)

    print("3) Count of rows in Dimension and Fact tables")
    q3 = """
    SELECT
        (SELECT COUNT(*) FROM dim_pokemon) AS dim_count,
        (SELECT COUNT(*) FROM fact_pokemon_stats) AS fact_count;
    """
    df3 = run_query(q3)
    print(df3)
    print("-" * 60)


if __name__ == "__main__":
    main()
