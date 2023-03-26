import { Link } from "react-router-dom";
import "./signup.css"
function Login() {
  return (
<div style={{ backgroundColor: "#212529", height: "100vh" }}>

<div className="form-container pt-5" id="">
        </div>
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
    <Link to="/Products" id="link">Skip login</Link>
    <br />
    <button type="submit" className="btn btn-warning mt-3">
      Sign in
    </button>
  </form>
</div>
</div>
  );
}

export default Login;
