import React, { useEffect, useState } from "react";

function ResultsView() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    loadResults();
  }, []);

  const loadResults = async () => {
    const response = await fetch("http://127.0.0.1:5000/results");
    const data = await response.json();
    setResults(data);
  };

  return (
    <div>
      <h2>Результати</h2>
      {results.length === 0 ? (
        <p>Немає відповідей</p>
      ) : (
        <table border="1" cellPadding="5">
          <thead>
            <tr>
              <th>Респондент</th>
              <th>Відповіді</th>
            </tr>
          </thead>
          <tbody>
            {results.map((r, i) => (
              <tr key={i}>
                <td>{r.user}</td>
                <td>{r.answers}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ResultsView;
