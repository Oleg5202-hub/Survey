import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Navbar from "./components/Navbar";
import SurveyForm from "./components/SurveyForm";
import QuestionEditor from "./components/QuestionEditor";
import ResultsView from "./components/ResultsView";
import "./styles/theme.css";
import "./styles/layout.css";
import "./styles/components.css";

function App() {
  return (
    <Router>
      <Layout>
        <Navbar />
        <Routes>
          <Route path="/edit" element={<QuestionEditor />} />
          <Route path="/survey" element={<SurveyForm />} />
          <Route path="/results" element={<ResultsView />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
