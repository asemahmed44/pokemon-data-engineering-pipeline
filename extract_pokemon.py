import requests
import pandas as pd

def fetch_pokemon(limit=50):
    base_url = "https://pokeapi.co/api/v2/pokemon"
    pokemon_list = []

    for i in range(1, limit + 1):
        url = f"{base_url}/{i}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_list.append({
                "id": data["id"],
                "name": data["name"],
                "base_experience": data.get("base_experience"),
                "height": data.get("height"),
                "weight": data.get("weight")
            })
        else:
            print(f"Failed to fetch pokemon with id {i}")

    return pokemon_list

def main():
    print("Fetching Pokémon data...")
    pokemons = fetch_pokemon(limit=50)

    df = pd.DataFrame(pokemons)
    print("Sample data:")
    print(df.head())

    df.to_csv("raw_pokemon.csv", index=False)
    print("Saved raw data to raw_pokemon.csv")

if __name__ == "__main__":
    main()
