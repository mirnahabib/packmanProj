import React, { useState } from 'react';
import MyUser from './MyUser';

const MyUserProvider = ({ children }) => {
    const [user, setUser] = useState({
        "name": "",
        "role": "",
        "userId": ""
      });

      const [isLoggedIn, setIsLoggedIn] = useState(false);

  const updateState = (newValue) => {
    setUser(newValue);
  }

  const updateLogState = (newValue) => {
    setIsLoggedIn(newValue);
  }

  return (
    <MyUser.Provider value={{ user, isLoggedIn ,updateState , updateLogState }}>
      {children}
    </MyUser.Provider>
  );
};

export default MyUserProvider;