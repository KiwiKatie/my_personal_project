import React, { useState } from 'react';
import axios from 'axios';
import api from './utilities';
import { Link } from 'react-router-dom';


export default function Creator() {
    const [characterData, setCharacterData] = useState({
        name:'',
        charisma:0,
        dexterity:0,
        strength:0,
        intelligence:0,  
      });
      const [gameProgress, setGameProgress] = useState({
        last_battle:'none',
        damage:0,
        health:50,
        level:1,
        story_section:'Beginnings',  
      });
     
    const token = localStorage.token;

    const headers = {
        Authorization: `Token ${token}`,
      };
    

      const handleSubmit = async (e) => {
        e.preventDefault();
        alert("Character created. You may begin your adventure.")

        try {
            const response = await api.post('player/create/', characterData, { headers });
            const GameResponse = await api.put('player/progress/', gameProgress, { headers });
            
            setGameProgress((prevData) => ({
                ...prevData,
                story_section: 'Beginnings', 
            }));
        } catch (error) {
         }
    };

  const totalTraits = characterData.charisma + characterData.dexterity + characterData.strength + characterData.intelligence;
  const remainingPoints = 15 - totalTraits;

    const handleInputChange = (e) => {
    const { name, value } = e.target;
    if (name === 'name') {
      setCharacterData((prevData) => ({
        ...prevData,
        [name]: value,
      }));
    } else {

      const updatedValue = parseInt(value, 15);
      const limitedValue = Math.min(updatedValue, 15);
      const newRemainingPoints = 15 - totalTraits - limitedValue;

      setGameProgress((prevData) => ({
        ...prevData,
        [name]: limitedValue,
      }));

      setCharacterData((prevData) => ({
        ...prevData,
        [name]: limitedValue,
      }));

    }
  };

    return (
      <>
        <div className='character-container '>
        <h2>Create Your Character!</h2>
        </div>
      <div className="CreatorPageContainer">
      <div className="CreatorContainerWrapper">
      <div className='CreatorContainerStyle'>
        <p>You have {remainingPoints} points to assign </p>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Name:</label>
            <input
              type="text"
              name="name"
              value={characterData.name}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Charisma:</label>
            <input
              type="number"
              name="charisma"
              value={characterData.charisma}
              onChange={handleInputChange}
              min="0"
              max="15"
              disabled={remainingPoints === 0} 
            />
          </div>
          <div>
            <label>Dexterity:</label>
            <input
              type="number"
              name="dexterity"
              value={characterData.dexterity}
              onChange={handleInputChange}
              min="0"
              max="15"
              disabled={remainingPoints === 0} 
            />
          </div>
          <div>
            <label>Strength:</label>
            <input
              type="number"
              name="strength"
              value={characterData.strength}
              onChange={handleInputChange}
              min="0"
              max="15"
              disabled={remainingPoints === 0} 
            />
          </div>
          <div>
            <label>Intelligence:</label>
            <input
              type="number"
              name="intelligence"
              value={characterData.intelligence}
              onChange={handleInputChange}
              min="0"
              max="15"
              disabled={remainingPoints === 0} 
            />
          </div>
          <div>
          <button type="submit">Save Character Traits</button>
           <span style={{ margin: '0 10px' }}></span> 
            <Link to="/gamepage">
            <button type="button">Begin your adventure...</button>
             </Link>
          </div>
        </form>
      </div>
      </div>
      </div>
      </>
    );
  }
  