import { Link } from "react-router-dom";
import "./css/signup.css";
import { useGlobalContext } from '../context';

function Login() {
  return (
<div className="container align-items-center justify-content-center text-center p-5">

<div className="form-container text-white pt-5 ">

  <form
    className="form-data w-50 h-50 "
  >
    <div className="mb-3">
      <label className="form-label">Email address</label>
      <input
        type="email"
        className="form-control"
        placeholder="Enter your email..."
        aria-describedby="emailHelp"
        
      />
    </div>
    <div className="mb-3">
      <label className="form-label">Password</label>
      <input
        type="password"
        className="form-control"
        placeholder="Enter your password..."
      />
    </div>
    <Link to="/Signup" id="link">New user? signup now</Link>
    <br />
    <Link to="/" id="link">Skip login</Link>
    <br />
    <button type="submit" className="btn btn-warning mt-3">
      Sign in
    </button>
    <br />
  </form>
</div>
</div>
  );
}

export default Login;
