import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const [isAdmin, setIsAdmin] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const adminStatus = localStorage.getItem("is_admin");
    setIsAdmin(adminStatus === "true");
  }, []);

  const logout = () => {
    localStorage.clear();
    navigate("/login");
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Dashboard</h1>

      {isAdmin ? (
        <>
          <h3>Admin Panel</h3>
          <button onClick={() => navigate("/create-election")}>
            Create Election
          </button>
          <br /><br />
          <button onClick={() => navigate("/add-candidate")}>
            Add Candidate
          </button>
          <br /><br />
        </>
      ) : (
        <>
          <h3>User Panel</h3>
          <button onClick={() => navigate("/vote")}>
            Vote Now
          </button>
          <br /><br />
        </>
      )}

      <button onClick={() => navigate("/results")}>
        View Results
      </button>

      <br /><br />
      <button onClick={logout}>Logout</button>
    </div>
  );
}

export default Dashboard;