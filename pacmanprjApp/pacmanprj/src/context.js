import axios from 'axios';
import React, { useContext, useState, useEffect } from 'react';
import jwt_decode from 'jwt-decode';

const AppContext = React.createContext();

const AppProvider = ({ children }) => {
  const [isLoading, setIsLoading] = useState(true);
  const [user, setUser] = useState(null);

  const saveUser = (user) => {
    setUser(user);
  };

  const removeUser = () => {
    setUser(null);
  };

  const fetchUser = async () => {
    try {
      const { data } = await axios.get(`/api/users/showMe`);
      saveUser(data.user);
    } catch (error) {
      removeUser();
    }
    setIsLoading(false);
  };

  const logoutUser = async () => {
    try {
      await axios.delete('/api/auth/logout');
      removeUser();
    } catch (error) {
      console.log(error);
    }
  };

  function googleClientCallbackResonse(response){
    try{
    console.log("jwt google token: " + response.credential)
    var googleUser = jwt_decode(response.credential);
    saveUser(googleUser);   
    }catch (error) {
        console.log(error);
        removeUser();
      }
  }

  const googleClient = async () => {
    /* global google */
    google.accounts.is.initialize({
        client_id: "509262672064-ppiak8lk7ra2vscpsj29dt4fp0v9re4j.apps.googleusercontent.com",
        callback: googleClientCallbackResonse
      });
  }
  useEffect(() => {
    fetchUser();
    googleClient();
  }, []);

  return (
    <AppContext.Provider
      value={{
        isLoading,
        saveUser,
        user,
        logoutUser,
        googleClient,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
// make sure use
export const useGlobalContext = () => {
  return useContext(AppContext);
};

export { AppProvider };