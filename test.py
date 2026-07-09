import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
data = response.json()

print(data["abilities"])