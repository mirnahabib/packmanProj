import React from "react";
import './App.css';
import {BrowserRouter as Router, Routes , Route} from 'react-router-dom'
import Home from "./pages/Home";
import Login from "./component/login";
import "bootstrap/dist/css/bootstrap.min.css"
import Signup from "./component/signup";
function App() {
  return (
    
   <Router>
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/Login' element={<Login/>}/>
      <Route path='/signup' element={<Signup/>}/>
    </Routes>
   </Router>
  
  );
}
export default App;



