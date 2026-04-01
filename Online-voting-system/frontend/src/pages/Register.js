import React, { useState } from "react";
import API from "../api";
import { useNavigate } from "react-router-dom";

function Register() {
  const [data, setData] = useState({
    username: "",
    password: ""
  });

  const navigate = useNavigate();

  const handleRegister = async () => {
    try {
      await API.post("/auth/register", data);
      alert("Registration successful!");
      navigate("/login");
    } catch (err) {
      alert("Error registering user");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Register</h2>

      <input
        type="text"
        placeholder="Username"
        value={data.username}
        onChange={(e) =>
          setData({ ...data, username: e.target.value })
        }
      />
      <br /><br />

      <input
        type="password"
        placeholder="Password"
        value={data.password}
        onChange={(e) =>
          setData({ ...data, password: e.target.value })
        }
      />
      <br /><br />

      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;