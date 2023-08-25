import React, { useState } from 'react';
import axios from 'axios';
import api from './utilities';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import NavBar from './NavBar';

export default function GamePage (){
    const navigate = useNavigate();
    const [storyData, setStoryData] = useState([])
    const [currentPartIndex, setCurrentPartIndex] = useState(0);
    const [characterTraits, setCharacterTraits] = useState('');
    const [gameProgress, setGameProgress] = useState('');
    const [inventory, setInventory] = useState([])
    const [gameData, setGameData] = useState(null);
    const [monsterHealth, setMonsterHealth] = useState(0);
    const[monsterDamage, setMonsterDamage] = useState([])
    const [inCombat, setInCombat] = useState(false);
    const[playerDamage, setPlayerDamage] = useState([])
    const[playerHealth, setPlayerHealth] = useState(50)
    const [monsterName, setMonsterName] = useState("");
    const [attackChoice, setAttackChoice] = useState("")

//Tokens
    const token= localStorage.token;
    const headers = {
        Authorization: `Token ${token}`,
      };

// Monsters
      useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await api.get(
              "player/story/",
              { headers }
            );
            setGameData(response.data);
          } catch (error) {
            console.error(error);
          }
        };
        fetchData();
      }, []);

      const startCombat = async (monsterName) => {
        try {
          const response = await api.get(
            `monster/combat/${monsterName}/`,
            { headers }
          );
          setMonsterHealth(response.data.hit_points)
          setInCombat(true);
        } catch (error) {
          console.error(error);
        }
      };

      const handleCombatAttack = async (monsterName, attackChoice) => {
        try {
          const response = await api.put(
            `monster/combat/${monsterName}/`,
            { player_choice: attackChoice , monster_health: monsterHealth},
            { headers }
          );
      
          const { player_health, player_attack, monster_health, monster_attack } = response.data;
      
          setPlayerHealth(player_health);
          setMonsterHealth(monster_health);
          setPlayerDamage(player_attack);
          setMonsterDamage(monster_attack);
      
          if (player_health <= 0 || monster_health <= 0) {
            setInCombat(false);
          }
        } catch (error) {
          console.error(error);
        }
      };
// Traits
    useEffect(() => {
        const getTraits = async () => {
          try {
            const response = await api.get('player/traits/', { headers });
            setCharacterTraits(response.data);
          } catch (error) {
            console.error(error);
          }
        };
    
        getTraits(); 
      }, []);

// Health
useEffect(() => {
        const getHealth = async () => {
        try {
            const response = await api.get('/player/progress/', { headers });
            setGameProgress(response.data);
        } catch (error) {
            console.error(error);
        }
        };

    getHealth(); 
  }, []);

// Story
      useEffect(() => {
          async function fetchStoryData() {
              try {
                  const response = await api.get('player/story/', { headers });
                  setStoryData(response.data.Beginnings); 
                } catch (error) {
                    console.error(error);
                }
            }
            fetchStoryData();
        }, []);

        const checkRequirements = (requirements) => {
          for (const trait in requirements) {
            const requirement = requirements[trait];
            const characterTraitValue = characterTraits[trait];
            if (characterTraitValue < requirement.min) {
              return false;
            }
          }
          return true;
        };

        const handleChoiceSelect = (choiceIndex) => {
          const selectedChoice = storyData[currentPartIndex].choices[choiceIndex];
          if (selectedChoice.attack_choice) {
            setAttackChoice(selectedChoice.attack_choice);
          }
          if (selectedChoice) {
            
            if (selectedChoice.go_to) {
              if (selectedChoice.go_to === "combat") {
                  setMonsterName(selectedChoice.monsters);
                  startCombat(selectedChoice.monsters);
                  setCurrentPartIndex(storyData.findIndex(part => part.id === selectedChoice.go_to));
              } else if( !inCombat) {
                setCurrentPartIndex(storyData.findIndex(part => part.id === selectedChoice.go_to));
              } else if(selectedChoice.go_to === "battle_outcome"){
                handleCombatAttack(monsterName, selectedChoice.attack_choice)
              }
            }
            if (selectedChoice.requirements && !checkRequirements(selectedChoice.requirements)) {
              const defaultChoice = storyData[currentPartIndex].choices.find(choice => choice.default === true);
              if (defaultChoice && defaultChoice.go_to) {
                setCurrentPartIndex(storyData.findIndex(part => part.id === defaultChoice.go_to));
              }
          }
        }
        };


        return(
          <>
            <NavBar/>
              <div className="trait-status-container">
                <div className="trait-box">
                  <h2>Character Traits</h2>
                  <p>Charisma: {characterTraits.charisma}</p>
                  <p>Dexterity: {characterTraits.dexterity}</p>
                  <p>Strength: {characterTraits.strength}</p>
                  <p>Intelligence: {characterTraits.intelligence}</p>
                </div>
             
            <div className='game-page'>
              <div className='over-story'>
              </div>
              <div className="story-trait-inventory-container">
                <div className="story-box">
                  {storyData.length > 0 && (
                    <>
                      <p>{storyData[currentPartIndex].text}</p>
                      {inCombat && (
                        <div className="combat-info">
                          <p>Your Health: {playerHealth}</p>
                          <p>Monster Health: {monsterHealth}</p>
                          {!inCombat && battleOutcome && (
                            <div className="battle-outcome">
                              <p>{battleOutcome.message}</p>
                              {battleOutcome.message === 'You defeated the monster!' && (
                                <button onClick={() => handleChoiceSelect(0)}>Pick up coin and continue</button>
                              )}
                              {battleOutcome.message === 'You were defeated!' && (
                                <button onClick={() => handleChoiceSelect(0)}>Retry?</button>
                              )}
                            </div>
                          )}
                          {/* Display choices */}
                          {storyData.length > 0 && storyData[currentPartIndex]?.choices && inCombat && (
                        <div className="choices">
                        {storyData[currentPartIndex].choices.map((choice, index) => (
                          <button
                            key={index}
                            onClick={() => handleChoiceSelect(index)}
                          >
                            {choice.text}
                          </button>
                        ))}
                      </div>
                      
                      )}
                        </div>
                      )}
                      {storyData.length > 0 && storyData[currentPartIndex]?.choices && !inCombat && (
                        <div className="choices">
                          {storyData[currentPartIndex].choices.map((choice, index) => (
                            <button
                              key={index}
                              onClick={() => handleChoiceSelect(index)}
                              disabled={inCombat && !choice.attack} 
                            >
                              {choice.text}
                            </button>
                          ))}
                        </div>
                      )}
                    </>
                  )}
                </div>
                </div>
              </div>
                      <div  className="status-box">
                        <h2>Status</h2>
                        <p>Name: {characterTraits.name}</p>
                        <p>Health: {gameProgress.health}</p>
                        <p>Level: {gameProgress.level}</p>
                      </div>
            </div>
          </>
        );
        
     }
          
