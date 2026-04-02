import "../styles/card.css";

const SectionCard = ({ title, items }) => {
  return (
    <div className="card">

      <h3 className="card-title">{title}</h3>

      <ul className="card-list">
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

    </div>
  );
};

export default SectionCard;