from flask import Blueprint, request, jsonify
from .models import Survey, Question, Choice, Answer
from . import db

bp = Blueprint('bp', __name__)

@bp.route('/create_survey', methods=['POST'])
def create_survey():
    data = request.get_json()
    survey = Survey(title=data['title'], description=data.get('description'))
    db.session.add(survey)
    db.session.commit()
    return jsonify({"id": survey.id})

@bp.route('/add_question', methods=['POST'])
def add_question():
    data = request.get_json()
    question = Question(survey_id=data['survey_id'], text=data['text'], type=data['type'])
    db.session.add(question)
    db.session.commit()
    if 'options' in data:
        for opt in data['options']:
            choice = Choice(question_id=question.id, text=opt)
            db.session.add(choice)
        db.session.commit()
    return jsonify({"id": question.id, "text": question.text})

@bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    answer = Answer(
        survey_id=data['survey_id'],
        question_id=data['question_id'],
        value=data['value']
    )
    db.session.add(answer)
    db.session.commit()
    return jsonify({"id": answer.id, "value": answer.value})

@bp.route('/get_results/<int:survey_id>', methods=['GET'])
def get_results(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    results = {}
    for q in survey.questions:
        answers = [a.value for a in q.answers]
        options = [c.text for c in q.choices]
        results[q.text] = {'options': options, 'answers': answers}
    return jsonify(results)
