import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import api from './utilities';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      let response = await api.post('/user/login/', { email, password });
      console.log(response.data);
      setEmail('');
      setPassword('');
      console.log(response.data)
      localStorage.setItem("token", response.data);
        api.defaults.headers.common["Authorization"] = `Token ${response.data}`;
        navigate("/gamepage");
    } catch (error) {
      console.error(error);
    }
  };


  return (
    <div className="LoginSignupContainerStyle">
      <h2 className="Login-Signup">Login</h2>
      <form className="email-password">
        <div className='email'>
          <input type="email" value={email} placeholder="Email" onChange={handleEmailChange} />
        </div>
        <div className='password'>
          <input type="password" value={password} placeholder="Password" onChange={handlePasswordChange} />
        </div>
        <button type="button" onClick={handleLogin}>Login</button>
      </form>
      <p>Don't have an account? <Link to="/signup">Sign Up</Link></p>
    </div>
  );
}

