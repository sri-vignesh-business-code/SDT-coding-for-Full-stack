import React, { useState } from "react";
import API from "../api";

function Login() {
  const [data, setData] = useState({ username: "", password: "" });

  const handleLogin = async () => {
    const res = await API.post("/auth/login", data);
    localStorage.setItem("token", res.data.token);
  };

  return (
    <div>
      <input placeholder="Username" onChange={e => setData({...data, username: e.target.value})}/>
      <input placeholder="Password" type="password" onChange={e => setData({...data, password: e.target.value})}/>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;