from .database import db
from .models import Survey, Question, Choice, Answer

def create_survey(title, description):
    survey = Survey(title=title, description=description)
    db.session.add(survey)
    db.session.commit()
    return survey

def add_question(survey_id, text, q_type, choices=None):
    question = Question(survey_id=survey_id, text=text, type=q_type)
    db.session.add(question)
    db.session.commit()

    if q_type == 'choice' and choices:
        for c in choices:
            choice = Choice(question_id=question.id, text=c)
            db.session.add(choice)
        db.session.commit()

    return question

def submit_answer(survey_id, question_id, value, user_id=None):
    answer = Answer(survey_id=survey_id, question_id=question_id, value=value, user_id=user_id)
    db.session.add(answer)
    db.session.commit()
    return answer

def get_results(survey_id):
    questions = Question.query.filter_by(survey_id=survey_id).all()
    results = {}
    for q in questions:
        answers = Answer.query.filter_by(question_id=q.id).all()
        results[q.text] = [a.value for a in answers]
    return results
