import React from "react";
import { useState, useEffect, useContext } from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import Home from "./pages/Home";
import "bootstrap/dist/css/bootstrap.min.css";
import Search from "./component/Search";
import "@fontsource/press-start-2p";
import "./component/css/style.css";
import Announcer from "./component/announcer";
import Home from "./component/Home";
import Team from "./component/about";
import Navingbar from "./component/navbar";
import SignUpForm from "./component/signupform";
import LoginForm from "./component/loginform";
import axios from "axios";
import MyUser from "./Contexts/MyUser";
import Favourites from "./component/favourites";

function App() {
  const { search } = window.location;
  const query = new URLSearchParams(search).get("s");
  const [searchQuery, setSearchQuery] = useState(query || "");
  const {  updateLogState ,isLoggedIn} = useContext(MyUser);
  

  const googleClientCallbackResponse = async (response) => {
    try {
      const authCode = response.credential;
      try {
        const { data } = await axios.post(
          "/api/auth/oauth/google",
          { authCode },
          { withCredentials: true }
        );
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${data["token"]}`;
        updateLogState(true);
        //console.log(data);
      } catch (error) {
        alert("failed to login");
        console.log(error);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const googleClientLogin = async () => {
    /* global google */
    google.accounts.id.initialize({
      client_id:
        "509262672064-ppiak8lk7ra2vscpsj29dt4fp0v9re4j.apps.googleusercontent.com",
      callback: googleClientCallbackResponse,
    });
    google.accounts.id.prompt();
  };

  useEffect(() => {
    // console.log(isLoggedIn);
    if (!isLoggedIn) { // Check if user is not logged in
      googleClientLogin();
    }
  }, [isLoggedIn]);

  return (
    <Router>
      <div className="App">
        <Navingbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<Team />} />
          <Route path="/fav" element={<Favourites/> }/>
          <Route path="/signup" element={<SignUpForm />} />
          <Route path="/login" element={<LoginForm />} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;
