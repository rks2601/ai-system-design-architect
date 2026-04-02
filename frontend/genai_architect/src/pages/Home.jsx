import { useState } from "react";
import InputBox from "../components/InputBox";
import Tabs from "../components/Tabs";
import { mockResponse } from "../mock/mockData";

import "../styles/home.css";

const Home = () => {
  const [result, setResult] = useState(null);

  const handleGenerate = (idea) => {
    console.log("User Idea:", idea);

    setTimeout(() => {
      setResult(mockResponse);
    }, 1000);
  };

  return (
    <div className="home-container">
      <div className="home-hero">
        <div className="hero-badge">AI ARCHITECT</div>

        <h1 className="title">🧠 AI System Design Architect</h1>

        <p className="subtitle">
          Generate scalable architecture and infrastructure plans in seconds
          with an AI-first workflow.
        </p>
      </div>

      <InputBox onGenerate={handleGenerate} />

      <div className="output-container">
        {result ? (
          <Tabs data={result} />
        ) : (
          <p className="empty-state">
            Enter an idea to generate system architecture
          </p>
        )}
      </div>
    </div>
  );
};

export default Home;
