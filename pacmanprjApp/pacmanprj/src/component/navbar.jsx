import React, { useState } from "react";
import {
  Navbar,
  Nav,
  Container,
  Dropdown,
  DropdownButton,
} from "react-bootstrap";
import { useContext } from "react";
import MyUser from "../Contexts/MyUser";
import { Link, Navigate } from "react-router-dom";
import packman from "./imgs/packman.png";
import NotificationsBell from "./notifications";


export default function Navingbar() {
  const { user, isLoggedIn, isUserSaved, logout } = useContext(MyUser); //want to access the global variables user,isLoggedIn in this component

  const handleOptionClick = (option) => {
    // console.log(`Selected ${option}`);
    if (option === "LOGOUT") logout();
  };

  return (
    <Navbar expand="lg" className="Navbar sticky-top">
      <Container>
        <Navbar.Brand>
          {" "}
          <Nav.Link as={Link} to="/">
            <img src={packman} className="navbar-logo" alt="pacman logo" />{" "}
          </Nav.Link>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbar-nav" />
        <Navbar.Collapse id="navbar-nav">
          <Nav>
            <Nav.Link as={Link} to="/" className="Font navbar-text">
              Home
            </Nav.Link>

            {isLoggedIn ? (
              ""
            ) : (
              <Nav.Link as={Link} to="/login" className="Font navbar-text">
                Login
              </Nav.Link>
            )}
            {isLoggedIn ? (
              ""
            ) : (
              <Nav.Link as={Link} to="/Signup" className="Font navbar-text">
                Signup
              </Nav.Link>
            )}
            <Nav.Link as={Link} to="/about" className="Font navbar-text">
              About
            </Nav.Link>

            {/* <Nav.Link as={Link} to="/notifications" className="Font navbar-text">
              Notifications
            </Nav.Link> */}

            

          </Nav>
        </Navbar.Collapse>
        <Navbar.Collapse className="justify-content-end">
          {isLoggedIn && isUserSaved ? (
            <div>
              <DropdownButton
                className="pe-3"
                title={user.name}
                variant="primary"
                onSelect={(eventKey) => handleOptionClick(eventKey)}
              >
                <Dropdown.Item as={Link} to="/fav">
                  Favourites
                </Dropdown.Item>
                <Dropdown.Item eventKey="LOGOUT">Logout</Dropdown.Item>
              </DropdownButton>
              
            </div>
          ) : (
            ""
          )}
          <NotificationsBell />
        </Navbar.Collapse>
      </Container>
      
    </Navbar>
  );
}
