import requests

BASE_URL = "http://127.0.0.1:5000"

answers = [
    {"survey_id": 1, "question_id": 1, "value": "Так"},
    {"survey_id": 1, "question_id": 2, "value": "Ні"},
    {"survey_id": 1, "question_id": 3, "value": "Можливо"},
]

for ans in answers:
    response = requests.post(f"{BASE_URL}/submit_answer", json=ans)
    print(response.status_code, response.text)
