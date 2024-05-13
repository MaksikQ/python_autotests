import pytest
import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TRAINER_TOKEN'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '2192'

def test_status_code():
    response_trainers = requests.get(url = f'{URL}/trainers', headers= HEADERS, params = {'trainer_id' : TRAINER_ID})
    assert response_trainers.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', headers= HEADERS, params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"]== 'Ranger'
    