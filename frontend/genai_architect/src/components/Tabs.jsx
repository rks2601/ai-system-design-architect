import { useState } from "react";
import "../styles/tabs.css";

const Tabs = ({ data }) => {
  const [activeTab, setActiveTab] = useState("overview");

  const tabs = [
    { key: "overview", label: "Overview" },
    { key: "architecture", label: "Architecture" },
    { key: "database", label: "Database" },
    { key: "scaling", label: "Scaling" },
    { key: "risks", label: "Risks" }
  ];

  return (
    <div className="tabs-container">

      {/* Tabs */}
      <div className="tabs-header">
        {tabs.map((tab) => (
          <button
            key={tab.key}
            className={activeTab === tab.key ? "tab active" : "tab"}
            onClick={() => setActiveTab(tab.key)}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Content */}
      <div className="tabs-content">

        {activeTab === "overview" && (
          <>
            <h3>Functional Requirements</h3>
            <ul>
              {data.functional_requirements.map((item, i) => (
                <li key={i}>{item}</li>
              ))}
            </ul>

            <h3>Non-Functional Requirements</h3>
            <ul>
              {data.non_functional_requirements.map((item, i) => (
                <li key={i}>{item}</li>
              ))}
            </ul>
          </>
        )}

        {activeTab === "architecture" && (
          <ul>
            {data.architecture_components.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>
        )}

        {activeTab === "database" && (
          <ul>
            {data.database_design.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>
        )}

        {activeTab === "scaling" && (
          <ul>
            {data.scaling_strategy.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>
        )}

        {activeTab === "risks" && (
          <ul>
            {data.risks.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>
        )}

      </div>
    </div>
  );
};

export default Tabs;