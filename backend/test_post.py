from app.models import create_survey, add_question, submit_answer, get_results

def test_create_survey():
    created_id = create_survey("Футбольне опитування", "Опитування для фанатів футболу")
    assert created_id == 1

def test_add_question():
    question_id = add_question(1, "Хто виграє Лігу Чемпіонів?")
    assert question_id == 1

def test_submit_answer():
    answer_id = submit_answer(1, "Реал Мадрид")
    assert answer_id == 1

def test_get_results():
    results = get_results(1)
    assert results == {"Реал Мадрид": 1}
