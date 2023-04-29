import React from 'react'
import { Navbar, Nav, Container } from "react-bootstrap";
import { useContext } from 'react';
import MyUser from "../Contexts/MyUser";
import { Link } from 'react-router-dom';

import logo from "./imgs/logo.png";
import packman from "./imgs/packman.png"

export default function Navingbar() {
  const {user,isLoggedIn, logout} = useContext(MyUser) //want to access the global variables user,isLoggedIn in this component

  // function show()
  // {
  //   console.log(user);
  // }
  return (
    <Navbar expand="lg" className="Navbar sticky-top" >
          <Container>
            <Navbar.Brand > <img src= {packman} className='navbar-logo'  alt='pacman logo' /> </Navbar.Brand>
            <Navbar.Toggle aria-controls="navbar-nav" />
            <Navbar.Collapse id="navbar-nav">
              <Nav>
                <Nav.Link as={Link} to="/" className="Font navbar-text">Home</Nav.Link>
                {isLoggedIn ? "" : <Nav.Link as={Link} to="/login" className="Font navbar-text">Login</Nav.Link>}
                {isLoggedIn ? "" : <Nav.Link as={Link} to="/Signup" className="Font navbar-text">Signup</Nav.Link>}
                <Nav.Link as={Link} to="#" className="Font navbar-text">Favorites</Nav.Link>
                <Nav.Link as={Link} to="/team" className="Font navbar-text">Team</Nav.Link>
                
              </Nav>
              
            </Navbar.Collapse>
            
          </Container>
          {/* <button onClick={show}>Testing</button> */}
          {
            isLoggedIn ? 
            <div>
              <p className='align-self-end Font pe-3'>hi {user.name}</p>
              <button className='pe-5 btn btn-danger' onClick = {logout}>Logout</button>
            </div> : ""
          }
         
        </Navbar>
  )
}
