import React, { useEffect, useState } from "react";
import API from "../api";

function Results() {
  const [results, setResults] = useState([]);

  useEffect(() => {
    const fetchResults = async () => {
      const res = await API.get("/results/1");
      setResults(res.data);
    };

    fetchResults();
    const interval = setInterval(fetchResults, 3000); // real-time polling
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      {results.map((r, i) => (
        <p key={i}>{r.candidate}: {r.votes}</p>
      ))}
    </div>
  );
}

export default Results;