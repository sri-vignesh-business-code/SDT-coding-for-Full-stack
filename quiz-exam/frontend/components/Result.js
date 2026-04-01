import { useLocation } from "react-router-dom";

function Result() {
  const { state } = useLocation();

  return (
    <div>
      <h2>Result</h2>
      <p>Score: {state.score} / {state.total}</p>
    </div>
  );
}

export default Result;