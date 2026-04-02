import { useState } from "react";
import "../styles/input.css";

const InputBox = ({ onGenerate }) => {
  const [idea, setIdea] = useState("");

  return (
    <div className="input-container">

      <input
        className="input-box"
        type="text"
        placeholder="Design Instagram for 10M users"
        value={idea}
        onChange={(e) => setIdea(e.target.value)}
      />

      <button
        className="generate-btn"
        onClick={() => onGenerate(idea)}
      >
        🚀 Generate
      </button>

    </div>
  );
};

export default InputBox;