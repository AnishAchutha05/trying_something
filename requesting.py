import requests
import json

pokemon = input("Enter a pokemon name: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()   

    with open("Names.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data saved successfully ✅")
else:
    print("Pokemon not found ❌")
