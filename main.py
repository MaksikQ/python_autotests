import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TRAINER_TOKEN'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

# Создать покемона
body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response_create = requests.post(url = f'{URL}/pokemons', headers= HEADERS, json = body_create)

id_new_pokemon = response_create.json()['id']
print(response_create.text)

# Сменить имя
body_new_name = {
    "pokemon_id": id_new_pokemon,
    "name": "New Name"
}

response_new_name = requests.patch(url = f'{URL}/pokemons', headers = HEADERS, json = body_new_name)

print(response_new_name.text)

# Поймать в покебол
body_add_pokeball = {
    "pokemon_id": id_new_pokemon
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_add_pokeball)
print(response_add_pokeball.text)

# Отправить в нокаут 
'''body_knockout = {
    "pokemon_id": "27152"
}

response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADERS, json = body_knockout)

print(response_knockout.text)'''
