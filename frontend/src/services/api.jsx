const API_URL = "http://localhost:5000";

export async function getQuestions() {
  const response = await fetch(`${API_URL}/questions`);
  return await response.json();
}

export async function saveQuestions(questions) {
  const response = await fetch(`${API_URL}/questions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ questions })
  });
  return await response.json();
}

export async function sendAnswers(answers) {
  const response = await fetch(`${API_URL}/answers`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answers })
  });
  return await response.json();
}

export async function getResults() {
  const response = await fetch(`${API_URL}/results`);
  return await response.json();
}
