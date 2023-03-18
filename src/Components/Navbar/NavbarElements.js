import styled from "styled-components";
import { NavLink as Link } from "react-router-dom";
import {FaBars} from 'react-icons/fa'


export const Nav= styled.nav`
background:#296d98;
height:80px;
display: flex;
justify-content: space between;
padding: 0.5rem calc((100vw - 1000px)/2);
z-index:10;
`
export const NavLink= styled(Link)`
color: #ffff00;
display: flex;
align-items:center;
text-decoration: none;
padding: 0 1rem;
height: 100%;
cursor:pointer;
&.active{
    color:#15cdfc;
}
`
export const Bars=styled(FaBars)`
display: none;
color:#0e2433;
@media screen and (max-width:768px)
{
    display:block;
    position: absolute;
    top:0;
    right:0;
    transform:translate(-100%, 75%);
    font-size: 1.8rem;
    cursor:pointer;
}
`
export const NavMenu= styled.div`
display: flex;
align-items:center;
margin-right:-24px;

@media screen and (max-wodth:768px)
{
    display:none;
}
`
export const NavBtn= styled.nav`
display:flex;
align-items:center;
margin-right: 24px;

@media screen and (max-width=768px)
{
    display:none;
}
`
export const NavbtnLink= styled(Link)`
 border-raduis:4px;
 background: #256ce1;
 padding: 10 px 22px;
 color:#fff;
 border:none;
 outline:none;
 cursor: pointer;
 transition: all 0.2s ease-in-out;
 text-decoration: none;
 &:hover{
    transition: all 0.2s ease-in-out;
    background:#fff00;
    color:#010606;
 }

`