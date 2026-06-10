import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function QuestionEditor() {
  const [questions, setQuestions] = useState([
    { text: "", options: ["", "", "", ""] },
    { text: "", options: ["", "", "", ""] },
    { text: "", options: ["", "", "", ""] },
    { text: "", options: ["", "", "", ""] }
  ]);
  const navigate = useNavigate();

  const handleQuestionChange = (index, value) => {
    const newQuestions = [...questions];
    newQuestions[index].text = value;
    setQuestions(newQuestions);
  };

  const handleOptionChange = (qIndex, oIndex, value) => {
    const newQuestions = [...questions];
    newQuestions[qIndex].options[oIndex] = value;
    setQuestions(newQuestions);
  };

  const handleSubmit = async () => {
    const prepared = questions.map(q => ({
      text: q.text,
      options: q.options.filter(o => o.trim() !== "")
    }));
    await fetch("http://127.0.0.1:5000/add_questions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ questions: prepared })
    });
    navigate("/survey");
  };

  return (
    <div>
      <h2>Редагування питань</h2>
      {questions.map((q, qi) => (
        <div key={qi} style={{ marginBottom: "20px" }}>
          <input
            type="text"
            placeholder={`Текст питання ${qi + 1}`}
            value={q.text}
            onChange={(e) => handleQuestionChange(qi, e.target.value)}
          />
          {q.options.map((opt, oi) => (
            <input
              key={oi}
              type="text"
              placeholder={`Варіант ${oi + 1}`}
              value={opt}
              onChange={(e) => handleOptionChange(qi, oi, e.target.value)}
            />
          ))}
        </div>
      ))}
      <button onClick={handleSubmit}>Зберегти всі</button>
    </div>
  );
}

export default QuestionEditor;
