import React from "react";
import { useState, useEffect } from 'react';
import './App.css';
import {BrowserRouter as Router, Routes , Route} from 'react-router-dom'
import Home from "./pages/Home";
import "bootstrap/dist/css/bootstrap.min.css"
import Search from "./component/Search";
import "@fontsource/press-start-2p";
import "./component/css/style.css";
import Announcer from './component/announcer';
import Product from "./component/product";
import Team from "./component/team";
import Navingbar from "./component/navbar";
import SignUpForm from "./component/signupform";
import LoginForm from "./component/loginform";
import { useGlobalContext } from './context';
import jwt_decode from 'jwt-decode';


import MyUserProvider from "./Contexts/MyUserProvider";  //parent to share variables with components




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
  const query = new URLSearchParams(search).get('s');
  const [searchQuery, setSearchQuery] = useState(query || '');

  function googleClientCallbackResonse(response){
    try{
    console.log("jwt google token: " + response.credential)
    var googleUser = jwt_decode(response.credential);
    //saveUser(googleUser);   
    }catch (error) {
        console.log(error);
      }
  }
  
  const googleClientLogin = async () => {
    /* global google */
    google.accounts.id.initialize({
        client_id: "509262672064-ppiak8lk7ra2vscpsj29dt4fp0v9re4j.apps.googleusercontent.com",
        callback: googleClientCallbackResonse
      });
    google.accounts.id.prompt();
  }
  
  useEffect(() => {
    googleClientLogin();
  }, []);
  
  // const filteredPosts = filterPosts(posts, searchQuery);
   return (
   <MyUserProvider>
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
        <Navingbar/>
      <Routes>
        <Route path='/' element={<Product/>}/>
        <Route path='/Team' element={<Team/>}/>
        <Route path='/signup' element={<SignUpForm/>}/>
        <Route path='/login' element={<LoginForm/>}/>
      </Routes>
    

      </div>

      
   </Router>
   </MyUserProvider>
  ); 
}
export default App;



