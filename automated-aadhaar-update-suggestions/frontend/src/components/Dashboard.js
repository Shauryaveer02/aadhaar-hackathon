import { useEffect, useState } from "react";
import { fetchSuggestions } from "../services/api";
import SuggestionCard from "./SuggestionCard";

function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchSuggestions().then(setData);
  }, []);

  return (
    <div>
      <h2>Automated Aadhaar Update Suggestions</h2>
      {data.map((item, index) => (
        <SuggestionCard key={index} data={item} />
      ))}
    </div>
  );
}

export default Dashboard;
