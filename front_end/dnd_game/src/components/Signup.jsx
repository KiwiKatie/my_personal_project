import React, { useState } from 'react';
import axios from 'axios';
import api from './utilities';
import { Link } from 'react-router-dom';
import Creator from './Creator';
import { useNavigate } from 'react-router-dom';

export default function Signup() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [user, setUser] = useState('');


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let response = await api.post('/user/signup/', { email, password });
      console.log(response.data);
      setEmail('');
      setPassword('');
      let user = response.data.user;
      let token = response.data.token;
      console.log(token)
      localStorage.setItem("token", token);
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        setUser(user);
        navigate("/creator");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
    {/* Signup */}
    <div className="LoginSignupContainerStyle">
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit} className="email-password">
      <div className="email">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}/>
          </div>
          <div className="password">
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        </div>
        <div>
        <button type="submit">Sign Up</button>
        </div>
      </form>

      <p>Already have an account? <Link to="/login">Login</Link></p>

    </div>
    </>
  );
};

