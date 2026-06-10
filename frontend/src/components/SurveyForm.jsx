import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function SurveyForm() {
  const [questions, setQuestions] = useState([
    { id: 1, text: "Вік", options: ["до 25", "25-45", "45+"] },
    { id: 2, text: "Стать", options: ["Чоловік", "Жінка"] },
    { id: 3, text: "Чи подобається сервіс?", options: ["Так", "Ні"] }
  ]);
  const [answers, setAnswers] = useState({});
  const navigate = useNavigate();

  useEffect(() => {
    loadQuestions();
  }, []);

  const loadQuestions = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/get_questions");
      const data = await response.json();
      if (data.length > 0) {
        setQuestions((prev) => [...prev, ...data]);
      }
    } catch (e) {}
  };

  const handleAnswer = (qid, answer) => {
    setAnswers({ ...answers, [qid]: answer });
  };

  const handleSubmit = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/results");
      const existing = await res.json();
      const nextId = existing.length + 1;

      await fetch("http://127.0.0.1:5000/save_answers", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user: `Респондент ${nextId}`, answers })
      });
      navigate("/results");
    } catch (e) {}
  };

  return (
    <div>
      <h2>Опитування</h2>
      {questions.map((q) => (
        <div key={q.id}>
          <p>{q.text}</p>
          {q.options.map((opt, i) => (
            <button
              key={i}
              onClick={() => handleAnswer(q.id, opt)}
              style={{
                backgroundColor: answers[q.id] === opt ? "lightgreen" : "white"
              }}
            >
              {opt}
            </button>
          ))}
          {answers[q.id] && <p>Вибрано: {answers[q.id]}</p>}
        </div>
      ))}
      <button onClick={handleSubmit}>Надіслати</button>
    </div>
  );
}

export default SurveyForm;
