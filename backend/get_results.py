import requests
import json

BASE_URL = "http://127.0.0.1:5000"

response = requests.get(f"{BASE_URL}/get_results/1")
print(json.dumps(response.json(), ensure_ascii=False, indent=2))
