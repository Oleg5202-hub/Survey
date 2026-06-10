import requests

BASE_URL = "http://127.0.0.1:5000"
survey_id = 1

response = requests.get(f"{BASE_URL}/get_results/{survey_id}")
print(response.status_code)
print(response.json())
