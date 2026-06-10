import pytest
from app import create_app, db
from app.models import Survey, Question, Option, Answer

@pytest.fixture
def app_context():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app

def test_models(app_context):
    survey = Survey(title="Футбол", description="Тест")
    db.session.add(survey)
    db.session.commit()
    q = Question(survey_id=survey.id, text="За яку команду?", type="choice")
    db.session.add(q)
    db.session.commit()
    o1 = Option(question_id=q.id, text="Динамо")
    o2 = Option(question_id=q.id, text="Шахтар")
    db.session.add_all([o1, o2])
    db.session.commit()
    a = Answer(survey_id=survey.id, question_id=q.id, value="Динамо")
    db.session.add(a)
    db.session.commit()
    assert survey.id > 0
    assert q in survey.questions
    assert len(q.options) == 2
    assert q.answers[0].value == "Динамо"
