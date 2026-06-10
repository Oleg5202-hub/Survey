import requests

BASE = "http://127.0.0.1:5000"

survey = requests.post(f"{BASE}/create_survey", json={
    "title": "Football survey",
    "description": "Survey for football fans"
}).json()
print(survey)
survey_id = survey["id"]

q1 = requests.post(f"{BASE}/add_question", json={
    "survey_id": survey_id,
    "text": "Your age?",
    "type": "text"
}).json()
print(q1)

q2 = requests.post(f"{BASE}/add_question", json={
    "survey_id": survey_id,
    "text": "Your gender?",
    "type": "text"
}).json()
print(q2)

q3 = requests.post(f"{BASE}/add_question", json={
    "survey_id": survey_id,
    "text": "Do you like our service?",
    "type": "text"
}).json()
print(q3)

q4 = requests.post(f"{BASE}/add_question", json={
    "survey_id": survey_id,
    "text": "Which team do you support?",
    "type": "choice",
    "options": ["Dynamo Kyiv", "Shakhtar", "Barcelona", "Real Madrid"]
}).json()
print(q4)

q5 = requests.post(f"{BASE}/add_question", json={
    "survey_id": survey_id,
    "text": "Who was the man of the match?",
    "type": "choice",
    "options": ["Goalkeeper", "Defender", "Midfielder", "Forward"]
}).json()
print(q5)

q6 = requests.post(f"{BASE}/add_question", json={
    "survey_id": survey_id,
    "text": "What is your favorite league?",
    "type": "choice",
    "options": ["Premier League", "La Liga", "Serie A", "Ligue 1"]
}).json()
print(q6)

q7 = requests.post(f"{BASE}/add_question", json={
    "survey_id": survey_id,
    "text": "Who is your favorite football player?",
    "type": "choice",
    "options": ["Messi", "Ronaldo", "Mbappe", "Lewandowski"]
}).json()
print(q7)

results = requests.get(f"{BASE}/get_results/{survey_id}").json()
print(results)
