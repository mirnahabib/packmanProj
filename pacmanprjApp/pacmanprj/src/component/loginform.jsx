import React, { useState } from "react";
import { Form, Button, Container, Row, Col } from "react-bootstrap";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
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
    alert(`Email: ${email}\nPassword: ${password}`);
    setEmail("");
    setPassword("");
  };

  return (
    <div className=" container text-light email-font pt-5 blur-background">
      
      <Row className="justify-content-center">
        <Col lg={6}>
        <h3 className="Font border-bottom">Login</h3>
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
