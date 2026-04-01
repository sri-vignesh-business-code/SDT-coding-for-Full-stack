import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import API from "../api";

function Quiz() {
  const { id } = useParams();
  const [quiz, setQuiz] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    API.get(`/quiz/${id}`).then(res => setQuiz(res.data));
  }, [id]);

  const submitQuiz = () => {
    API.post("/result/submit", {
      user: "test_user",
      quiz_id: id,
      questions: quiz.questions
    }).then(res => {
      navigate("/result", { state: res.data });
    });
  };

  const handleSelect = (qIndex, option) => {
    const updated = { ...quiz };
    updated.questions[qIndex].selected = option;
    setQuiz(updated);
  };

  if (!quiz) return <div>Loading...</div>;

  return (
    <div>
      <h2>{quiz.title}</h2>
      {quiz.questions.map((q, i) => (
        <div key={i}>
          <p>{q.question}</p>
          {q.options.map(opt => (
            <button key={opt} onClick={() => handleSelect(i, opt)}>
              {opt}
            </button>
          ))}
        </div>
      ))}
      <button onClick={submitQuiz}>Submit</button>
    </div>
  );
}

export default Quiz;