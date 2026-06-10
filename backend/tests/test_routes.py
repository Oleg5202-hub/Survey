import pytest
from app import create_app, db
from app.models import Survey

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        db.drop_all()
        db.create_all()
    return app.test_client()

def test_create_survey(client):
    rv = client.post('/create_survey', json={"title": "Футбол", "description": "Тест"})
    assert rv.status_code == 200
    data = rv.get_json()
    assert "id" in data

def test_add_question_with_options(client):
    survey = client.post('/create_survey', json={"title": "Футбол"}).get_json()
    rv = client.post('/add_question', json={
        "survey_id": survey["id"],
        "text": "За яку команду?",
        "type": "choice",
        "options": ["Динамо", "Шахтар", "Барселона", "Реал"]
    })
    assert rv.status_code == 200
    data = rv.get_json()
    assert "id" in data

def test_submit_answer(client):
    survey = client.post('/create_survey', json={"title": "Футбол"}).get_json()
    q = client.post('/add_question', json={
        "survey_id": survey["id"],
        "text": "Хто лев матчу?",
        "type": "choice",
        "options": ["Воротар", "Захисник", "Півзахисник", "Нападник"]
    }).get_json()
    rv = client.post('/submit_answer', json={
        "survey_id": survey["id"],
        "question_id": q["id"],
        "value": "Нападник"
    })
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["value"] == "Нападник"
