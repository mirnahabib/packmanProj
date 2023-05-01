import React, { useState, useEffect, useContext } from "react";
import { Form, Button, Row, Col } from "react-bootstrap";
import axios from "axios";
import { Navigate } from "react-router-dom";
import MyUser from "../Contexts/MyUser";

// want to access the global setstates in this component
const SignupForm = () => {
  useEffect(() => {
    googleClientLogin();
  }, []);

  const { updateState, updateLogState } = useContext(MyUser);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [navigate, setNavigate] = useState(false);
  const { name, email, password, confirmPassword } = formData;

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
      text: "Sign up with Google instead",
      longtitle: true,
      scope: "openid profile email",
    });
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Validate input before submitting form
    if (name.length < 3) {
      alert("Name must be at least 3 letters long");
      return;
    }
    if (!isValidEmail(email)) {
      alert("Please enter a valid email address");
      return;
    }
    if (password.length < 6) {
      alert("Password must be at least 6 characters long");
      return;
    }
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    // Submit form
    alert(`Thank you for signing up, ${name}!`);

    //Token
    const { data } = await axios.post(
      "/api/auth/register",
      { name, email, password },
      { withCredentials: true }
    );
    axios.defaults.headers.common["Authorization"] = `Bearer ${data["token"]}`;
    updateState({
      name: data.user.name,
      role: data.user.role,
      userId: data.user.userId,
    });
    updateLogState(true);
    setNavigate(true);
  };

  if (navigate) {
    return <Navigate to="/" />;
  }

  const isValidEmail = (email) => {
    // Check if email matches email pattern
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
  };

  return (
    <div className=" container text-light email-font pt-5 blur-background">
      <Row className="justify-content-center">
        <Col lg={6}>
          <h3 className="Font border-bottom heartbeat">Create An Account</h3>
          <Form className="pt-2" onSubmit={handleSubmit}>
            <Form.Group controlId="formName">
              <Form.Label className="pt-2">Name</Form.Label>
              <Form.Control
                type="text"
                name="name"
                className="text-resp"
                placeholder="Enter Name"
                value={name}
                onChange={handleChange}
                minLength="3"
                required
              />
            </Form.Group>

            <Form.Group controlId="formEmail">
              <Form.Label className="pt-2">Email address</Form.Label>
              <Form.Control
                type="email"
                name="email"
                className="text-resp"
                placeholder="Enter email"
                value={email}
                onChange={handleChange}
                required
              />
            </Form.Group>

            <Form.Group controlId="formPassword">
              <Form.Label className="pt-2">Password</Form.Label>
              <Form.Control
                type="password"
                name="password"
                className="text-resp"
                placeholder="Enter password"
                value={password}
                onChange={handleChange}
                minLength="6"
                required
              />
            </Form.Group>

            <Form.Group controlId="formConfirmPassword">
              <Form.Label className="pt-2">Confirm Password</Form.Label>
              <Form.Control
                type="password"
                name="confirmPassword"
                className="text-resp"
                placeholder="Re-enter password"
                value={confirmPassword}
                onChange={handleChange}
                minLength="6"
                required
              />
            </Form.Group>

            <Button className="mt-4" variant="primary" type="submit">
              Sign up
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

export default SignupForm;
