import requests
import yaml



# Load config from YAML
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Extract values
API_KEY = config["alpaca"]["api_key"]
SECRET_KEY = config["alpaca"]["secret_key"]
BASE_URL = config["settings"]["base_url"]

# Prepare headers
HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY
}

# Make API call
response = requests.get(f"{BASE_URL}/v2/account", headers=HEADERS)

# Show results
if response.status_code == 200:
    account_info = response.json()
    print("Account status:", account_info["status"])
    print("Cash balance:", account_info["cash"])
    print("Buying power:", account_info["buying_power"])
else:
    print("Error:", response.status_code)
    print("Message:", response.text)
