# Test Code - Jason
from requests.auth import HTTPBasicAuth
import requests
from safe import api_key, acc_name

init_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+acc_name+"?api_key="+api_key
response = requests.get(init_url)
if response.status_code == 200:
    response_body = response.json()
    print(response_body)
    encrypted_account_id = response_body['id']
    # url = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+encrypted_account_id+"?api_key="+api_key
    url = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+encrypted_account_id+"?api_key="+api_key
    response = requests.get(url).json()
    print(response)