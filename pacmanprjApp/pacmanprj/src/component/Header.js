import React, { useState } from "react";
import {Link} from 'react-router-dom'
import './Header.css'
import {FaProductHunt,FaWindowClose} from 'react-icons/fa'
import {FiLogIn,FiUse,FiMenu,FiUser} from 'react-icons/fi'
import {FcAbout} from 'react-icons/fc'
import {GrFavorite} from 'react-icons/gr'



const Header = () => {
    const [active,setActive] = useState(false)
    const activateNav= () => {
        setActive(!active)
    }
  return (
    <div className={active? 'header' : 'header-mobile'}>
        <div className='menu-icon' onClick={activateNav}>
            {!active ? <FiMenu className='menu'/> :<FaWindowClose className='menu'/>}

        </div>
      <nav>
        <ul className={active ? 'ul-item' : 'ul-item oicon'}>
            <li>
                <FiLogIn className='icon'/>
                <Link to='/Login'> Login</Link>
            </li>
            <li>
                <FiUser className='icon'/>
                <Link to='/signup'> Signup</Link>
            </li>
            <li>
                <FaProductHunt className='icon'/>
                <Link to='/'> Products</Link>
            </li>
            <li>
                <GrFavorite className='icon'/>
                <Link to='/'> Favorites</Link>
            </li>
            <li>
                <FcAbout className='icon'/>
                <Link to='/'> About us</Link>
            </li>
            
   
        </ul>
      </nav>
    </div>
  )
}

export default Header


