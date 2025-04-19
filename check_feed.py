import requests
import yaml

# Load config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

API_KEY = config["alpaca"]["api_key"]
SECRET_KEY = config["alpaca"]["secret_key"]
BASE_URL = config["settings"]["base_url"]

HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY
}

url = f"{BASE_URL}/v2/account"
response = requests.get(url, headers=HEADERS)
print(response.json())