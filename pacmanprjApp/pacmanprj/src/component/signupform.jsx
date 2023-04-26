import React, { useState } from 'react';
import { Form, Button, Row, Col} from 'react-bootstrap';

const SignupForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const { name, email, password, confirmPassword } = formData;

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Validate input before submitting form
    if (name.length < 3) {
      alert('Name must be at least 3 letters long');
      return;
    }
    if (!isValidEmail(email)) {
      alert('Please enter a valid email address');
      return;
    }
    if (password.length < 6) {
      alert('Password must be at least 6 characters long');
      return;
    }
    if (password !== confirmPassword) {
      alert('Passwords do not match');
      return;
    }

    // Submit form
    alert(`Thank you for signing up, ${name}!`);
    // Clear form
    setFormData({
      name: '',
      email: '',
      password: '',
      confirmPassword: '',
    });
    console.log(name , email , password);
  };

  const isValidEmail = (email) => {
    // Check if email matches email pattern
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
  };

  return (

    <div  className=" container text-light email-font pt-5 blur-background">
         <Row className="justify-content-center">
        <Col lg={6}>
        <h3 className='Font border-bottom heartbeat'>Create An Account</h3>
        <Form className='pt-2' onSubmit={handleSubmit}>
      <Form.Group controlId='formName'>
        <Form.Label className='pt-2'>Name</Form.Label>
        <Form.Control
          type='text'
          name='name'
          className="text-resp"
          placeholder="Enter Name"
          value={name}
          onChange={handleChange}
          minLength='3'
          required
        />
      </Form.Group>

      <Form.Group controlId='formEmail'>
        <Form.Label className='pt-2'>Email address</Form.Label>
        <Form.Control
          type='email'
          name='email'
          className="text-resp"
          placeholder="Enter email"
          value={email}
          onChange={handleChange}
          required
        />
      </Form.Group>

      <Form.Group controlId='formPassword'>
        <Form.Label className='pt-2'>Password</Form.Label>
        <Form.Control
          type='password'
          name='password'
          className="text-resp"
          placeholder="Enter password"
          value={password}
          onChange={handleChange}
          minLength='6'
          required
        />
      </Form.Group>

      <Form.Group controlId='formConfirmPassword'>
        <Form.Label className='pt-2'>Confirm Password</Form.Label>
        <Form.Control
          type='password'
          name='confirmPassword'
          className="text-resp"
          placeholder="Re-enter password"
          value={confirmPassword}
          onChange={handleChange}
          minLength='6'
          required
        />
      </Form.Group>

      <Button  className='mt-4' variant='primary' type='submit'>
        Sign up
      </Button>
    </Form>
    </Col>
     </Row>
    </div>
     
    
  );
};

export default SignupForm;



