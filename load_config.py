import yaml

# Open and load the YAML config file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Accessing values from the config
api_key = config["alpaca"]["api_key"]
secret_key = config["alpaca"]["secret_key"]
base_url = config["settings"]["base_url"]

print("API Key:", api_key)
print("Secret Key:", secret_key)
print("Base URL:", base_url)