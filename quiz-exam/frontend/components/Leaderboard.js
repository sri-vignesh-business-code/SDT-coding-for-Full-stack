import { useEffect, useState } from "react";
import API from "../api";

function Leaderboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.get("/result/leaderboard").then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
      {data.map((r, i) => (
        <div key={i}>
          {r.user} - {r.score}
        </div>
      ))}
    </div>
  );
}

export default Leaderboard;