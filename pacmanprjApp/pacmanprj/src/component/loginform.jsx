import React, { useState } from "react";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
import axios from 'axios';
import { Navigate } from 'react-router-dom';
import Product from "./product";
import Navingbar from "./navbar";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [navigate, setNavigate] = useState(false);
  const [user, setUser] = useState({
    "name": "",
    "role": "",
    "userId": ""
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    // email validation
    const emailRegex = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,})+$/;
    if (!emailRegex.test(email)) {
      alert("Please enter a valid email address.");
      return;
    }

    // password validation
    if (password.length < 6) {
      alert("Password must be at least 6 characters long.");
      return;
    }

    // form submitted successfully
    // alert(`Successfully logged in`);

    //Cookies
    const { data } = await axios.post('/api/auth/login', { email, password }, { withCredentials: true });
    axios.defaults.headers.common['Authorization'] = `Bearer ${data['token']}`;
    setUser({
      "name": data.user.name,
      "role": data.user.role,
      "userId": data.user.userId
    });
    console.log(user);
    // setNavigate(true);
  };

  if (navigate) {
    return <Navigate to="/" />
  }
  
  return (
    <div className=" container text-light email-font pt-5 blur-background">
      
      <Row className="justify-content-center">
        <Col lg={6}>
        <h3 className="Font border-bottom heartbeat">Login</h3>
          <Form className="pt-2" onSubmit={handleSubmit}>
            <Form.Group controlId="formEmail">
              <Form.Label className="pt-2">Email address</Form.Label>
              <Form.Control
                type="email"
                placeholder="Enter email"
                value={email}
                className="text-resp"
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </Form.Group>

            <Form.Group controlId="formPassword">
              <Form.Label className="pt-2">Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter password"
                className="text-resp"
                value={password}
                minLength="6"
                required
                onChange={(e) => setPassword(e.target.value)}
              />
            </Form.Group>

            <Button className="mt-4" variant="primary" type="submit">
              Login
            </Button>
          </Form>
        </Col>
      </Row>
    </div>
  );
};

export default LoginForm;
