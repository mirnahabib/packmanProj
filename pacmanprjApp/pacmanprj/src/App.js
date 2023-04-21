import React from "react";
import { useState, useEffect } from 'react';
import './App.css';
import {BrowserRouter as Router, Routes , Route} from 'react-router-dom'
import Home from "./pages/Home";
import Login from "./component/login";
import "bootstrap/dist/css/bootstrap.min.css"
import Signup from "./component/signup";
import Search from "./component/Search";
import "@fontsource/press-start-2p";
import "./component/css/style.css";
import Announcer from './component/announcer';
import Test from "./component/test";
import Product from "./component/product";
import Team from "./component/team";
import { Navbar, Nav, Container } from "react-bootstrap";
import logo from "./component/imgs/logo.png";


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
      <Routes>
        <Route path='/' element={<Product/>}/>
        <Route path='/Team' element={<Team/>}/>
        
        {/* <Route path='/Login' element={<Login/>}/>
        <Route path='/signup' element={<Signup/>}/>
        <Route path='/test' element= {<Test/>}/> */}
      </Routes>
      <Navbar expand="lg" className="Navbar" >
          <Container>
            <Navbar.Brand > <img src= {logo}/> </Navbar.Brand>
            <Navbar.Toggle aria-controls="navbar-nav" />
            <Navbar.Collapse id="navbar-nav">
              <Nav>
                <Nav.Link href="#" className="Font">Home</Nav.Link>
                <Nav.Link href="#" className="Font">Login</Nav.Link>
                <Nav.Link href="#" className="Font">Signup</Nav.Link>
                <Nav.Link href="#" className="Font">Favorites</Nav.Link>
                <Nav.Link href="#" className="Font">Team</Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>

      </div>

      
   </Router>
  ); 
}
export default App;



