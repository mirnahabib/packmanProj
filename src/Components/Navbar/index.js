import React ,{useState} from 'react'
import { Link } from 'react-router-dom'
import { Nav,NavLink,Bars,NavMenu,NavBtn,NavbtnLink } from './NavbarElements'


const Navbar = () => {
  const [sidebar,setSidebar]= useState(false)
  const showSidebar=() => setSidebar(!sidebar)
  return (
    <>
      <Nav> 
        <NavLink to ="/">
           <img style ={{width:180,height:100}} src="./images/packmanx3.png"/>
        </NavLink>
       <Bars/>
       <NavMenu>
        <NavLink to="/login" activeStyle>
          Login
        </NavLink>
        <NavLink to="/Sign Up" activeStyle>
          Sign up
        </NavLink>
        <NavLink to="/categories" activeStyle>
          Categories
        </NavLink>
        
       </NavMenu>
      </Nav>
     
    </>
  )
}

export default Navbar
