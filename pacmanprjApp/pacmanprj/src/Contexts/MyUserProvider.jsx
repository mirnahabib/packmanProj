import React, { useState, useEffect } from 'react';
import MyUser from './MyUser';
import axios from 'axios';

const MyUserProvider = ({ children }) => {
    const [user, setUser] = useState({
        "name": "",
        "role": "",
        "userId": ""
      });
      //const [refreshToken, setrefreshToken] = useState(null)

      const [isLoggedIn, setIsLoggedIn] = useState(false);

      //Logout
      const logout = async () =>
      {
        await axios.delete('/api/auth/logout',{},{withCredentials: true});
        setUser({
          "name": "",
          "role": "",
          "userId": ""
        });
        updateLogState(false);
      }

      //Currently logged in user's information
      useEffect(() => 
      {
        (async() =>
        {
          const {data} = await axios.get('/api/users/showMe');
          setUser(data.user);
          updateLogState(true);
          //console.log(data.user);
        }
        )();
      },[]);


  const updateState = (newValue) => {
    setUser(newValue);
  }

  const updateLogState = (newValue) => {
    setIsLoggedIn(newValue);
  }

  return (
    <MyUser.Provider value={{ user, isLoggedIn ,updateState , updateLogState, logout }}>
      {children}
    </MyUser.Provider>
  );
};

export default MyUserProvider;