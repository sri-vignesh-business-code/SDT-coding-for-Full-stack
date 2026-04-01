import { useEffect, useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

function Dashboard() {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    API.get("/quiz").then(res => setQuizzes(res.data));
  }, []);

  return (
    <div>
      <h2>Available Quizzes</h2>
      {quizzes.map(q => (
        <div key={q._id}>
          <h3>{q.title}</h3>
          <Link to={`/quiz/${q._id}`}>Start</Link>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;