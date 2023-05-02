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
import Team from "./component/team";
import Navingbar from "./component/navbar";
import SignUpForm from "./component/signupform";
import LoginForm from "./component/loginform";
import axios from "axios";
import MyUser from "./Contexts/MyUser";
import Favourites from "./component/favourites";

// const posts = [
//   { id: '1', name: 'This first post is about React' },
//   { id: '2', name: 'This next post is about Preact' },
//   { id: '3', name: 'We have yet another React post!' },
//   { id: '4', name: 'This is the fourth and final post' },
// ];
// const filterPosts = (posts, query) => {
//   if (!query) {
//       return posts;
//   }

//   return posts.filter((post) => {
//       const postName = post.name.toLowerCase();
//       return postName.includes(query);
//   });
// };

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
    console.log(isLoggedIn);
    if (!isLoggedIn) { // Check if user is not logged in
      googleClientLogin();
    }
  }, [isLoggedIn]);



  // const filteredPosts = filterPosts(posts, searchQuery);
  return (
    <Router>
      <div className="App">
        {/* <Announcer message={`${filteredPosts.length} posts`} />   
        <Search searchQuery={searchQuery} setSearchQuery={setSearchQuery}/>
        <ul>
          {filteredPosts.map((post) => (
            <li key={post.id}>{post.name}</li>
          ))}
        </ul> */}
        {/* <Home/> */}
        <Navingbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Team" element={<Team />} />
          <Route path="/fav" element={<Favourites/> }/>
          <Route path="/signup" element={<SignUpForm />} />
          <Route path="/login" element={<LoginForm />} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;
