import React from 'react';
import { Outlet } from 'react-router-dom';
import { Link } from 'react-router-dom';
import Signup from './signup';
import Login from './login';



export default function Homepage (){
      
    const buttonStyle = {
        width: '200px',
        height: '150px',
        marginRight: '10px'
    }
    
    return (
        <>
        <div className='home'>
          {location.pathname === '/' && (
            <div className="landing-page">
             <div className="title-container">
              <h1>Quest for the Taco Bell</h1>
              </div>
              <div className="landing-buttons">
                <div>
                  <Link to="/login" style={{ textDecoration: 'none' }}>
                    <div className="LandingLogin">
                      <img
                        src="https://www.transparentpng.com/thumb/treasure/open-treasure-chest-png-images-24.png"
                        alt="Login"
                        style={buttonStyle}
                      />
                    </div>
                    <div className='button-label'>Log In</div>
                  </Link>
                </div>
                <div>
                  <Link to="/signup" style={{ textDecoration: 'none' }}>
                    <div className="LandingSignup" style={buttonStyle}>
                      <img
                        src="https://www.transparentpng.com/thumb/treasure/open-treasure-chest-png-images-24.png"
                        alt="Signup"
                        style={buttonStyle}
                      />
                    </div>
                    <div className='button-label'>Sign Up</div>
                  </Link>
                </div>
              </div>
            </div>
          )}
          </div>
        </>
      );
    }