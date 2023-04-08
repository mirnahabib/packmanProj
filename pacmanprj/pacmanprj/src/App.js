import React from "react";
import { useState, useEffect } from 'react';
import './App.css';
import {BrowserRouter as Router, Routes , Route} from 'react-router-dom'
import Home from "./pages/Home";
import Login from "./component/login";
import "bootstrap/dist/css/bootstrap.min.css"
import Signup from "./component/signup";
import Search from "./component/Search";
import Announcer from './component/announcer';

const posts = [
  { id: '1', name: 'This first post is about React' },
  { id: '2', name: 'This next post is about Preact' },
  { id: '3', name: 'We have yet another React post!' },
  { id: '4', name: 'This is the fourth and final post' },
];
const filterPosts = (posts, query) => {
  if (!query) {
      return posts;
  }

  return posts.filter((post) => {
      const postName = post.name.toLowerCase();
      return postName.includes(query);
  });
};

function App() {
  const[backenedData, setBackendData] = useState([{}])
  useEffect (() =>
    {
      fetch ("/api/search"). then ( response => response.json ()). then ( data =>
        { setBackendData(data) }
      )
    }, [])

  const { search } = window.location;
  const query = new URLSearchParams(search).get('s');
  const [searchQuery, setSearchQuery] = useState(query || '');
  const filteredPosts = filterPosts(posts, searchQuery);
   return (
   <Router>
      <div className="App">
        <Announcer message={`${filteredPosts.length} posts`} />   
        <Search searchQuery={searchQuery} setSearchQuery={setSearchQuery}/>
        <ul>
          {filteredPosts.map((post) => (
            <li key={post.id}>{post.name}</li>
          ))}
        </ul>
      </div>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/Login' element={<Login/>}/>
        <Route path='/signup' element={<Signup/>}/>
      </Routes>
   </Router>
  ); 
}
export default App;



