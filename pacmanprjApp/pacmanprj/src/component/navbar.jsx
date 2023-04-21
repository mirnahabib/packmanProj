import React from 'react'
import { Navbar, Nav, Container } from "react-bootstrap";

import logo from "./imgs/logo.png";

export default function Navingbar() {
  return (
    <Navbar expand="lg" className="Navbar sticky-top" >
          <Container>
            <Navbar.Brand > <img src= {logo} alt='pacman logo'/> </Navbar.Brand>
            <Navbar.Toggle aria-controls="navbar-nav" />
            <Navbar.Collapse id="navbar-nav">
              <Nav>
                <Nav.Link href="/" className="Font">Home</Nav.Link>
                <Nav.Link href="#" className="Font">Login</Nav.Link>
                <Nav.Link href="#" className="Font">Signup</Nav.Link>
                <Nav.Link href="#" className="Font">Favorites</Nav.Link>
                <Nav.Link href="/team" className="Font">Team</Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
  )
}
