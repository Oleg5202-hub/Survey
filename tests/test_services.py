import pytest
from app import create_app, db
from app.models import Survey, Question, Option

@pytest.fixture
def app_context():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app

def test_service_logic(app_context):
    survey = Survey(title="Футбол")
    db.session.add(survey)
    db.session.commit()
    q = Question(survey_id=survey.id, text="Улюблений чемпіонат?", type="choice")
    db.session.add(q)
    db.session.commit()
    opts = [Option(question_id=q.id, text=o) for o in ["АПЛ", "Ла Ліга", "Серія А", "Ліга 1"]]
    db.session.add_all(opts)
    db.session.commit()
    assert len(q.options) == 4
