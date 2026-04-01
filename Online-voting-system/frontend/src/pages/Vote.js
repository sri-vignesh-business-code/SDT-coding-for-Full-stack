import React, { useState } from "react";
import API from "../api";

function Vote() {
  const [candidateId, setCandidateId] = useState("");

  const vote = async () => {
    await API.post("/vote/cast", {
      election_id: 1,
      candidate_id: candidateId
    }, {
      headers: { Authorization: "Bearer " + localStorage.getItem("token") }
    });
  };

  return (
    <div>
      <input placeholder="Candidate ID" onChange={e => setCandidateId(e.target.value)} />
      <button onClick={vote}>Vote</button>
    </div>
  );
}

export default Vote;