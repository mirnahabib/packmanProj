import React, { useState, useEffect, useContext } from "react";
import { Form, Button, Row, Col } from "react-bootstrap";
import axios from "axios";
import { Navigate } from "react-router-dom";
import MyUser from "../Contexts/MyUser";

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [navigate, setNavigate] = useState(false);

  const { updateState, updateLogState } = useContext(MyUser); // want to access the global setstates in this component

  const googleClientCallbackResonse = async (response) => {
    try {
      const authCode = response.credential;
      try {
        const { data } = await axios.post(
          "/api/auth/oauth/google",
          { authCode },
          { withCredentials: true }
        );
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${data["token"]}`;
        updateLogState(true);
        setNavigate(true);
        console.log(data);
      } catch (error) {
        alert("failed to login");
        console.log(error);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const googleClientLogin = async () => {
    /* global google */
    google.accounts.id.initialize({
      client_id:
        "509262672064-ppiak8lk7ra2vscpsj29dt4fp0v9re4j.apps.googleusercontent.com",
      callback: googleClientCallbackResonse,
    });
    google.accounts.id.renderButton(document.getElementById("googleSignIn"), {
      theme: "filled_blue",
      size: "large",
      width: "auto",
      height: 50,
      text: "Sign in with Google",
      longtitle: true,
      scope: "openid profile email",
    });
  };

  useEffect(() => {
    googleClientLogin();
  }, []);

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
    try {
      const { data } = await axios.post(
        "/api/auth/login",
        { email, password },
        { withCredentials: true }
      );
      axios.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${data["token"]}`;
      updateState({
        name: data.user.name,
        role: data.user.role,
        userId: data.user.userId,
      });
      updateLogState(true);
      setNavigate(true);
      console.log(data);
    } catch (error) {
      alert("failed to login");
      console.log(error);
    }
  };

  if (navigate) {
    return <Navigate to="/" />;
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

            <div class="d-flex justify-content-center pt-3">
              <div id="googleSignIn"></div>
            </div>
          </Form>
        </Col>
      </Row>
    </div>
  );
};

export default LoginForm;
