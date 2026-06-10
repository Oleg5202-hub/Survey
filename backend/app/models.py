from . import db

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    questions = db.relationship('Question', backref='survey', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(50))
    choices = db.relationship('Choice', backref='question', lazy=True)
    answers = db.relationship('Answer', backref='question', lazy=True)

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_id = db.Column(db.Integer, db.ForeignKey('choice.id'))
    value = db.Column(db.String(500))
