import { useForm } from "react-hook-form";
import "./css/signup.css";
function Signup() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();
  const onSubmit = (data) => {
    console.log(data);
    alert("signed up successfully");
  };

  return (
    
    <div style={{ backgroundColor: "#212529", height: "100vh" }}>

    
      <div className="form-container text-white pt-5 ">
        <form
          onSubmit={handleSubmit(onSubmit)}
          className="form-data w-50 h-50 "
        >
          <div className="mb-3 ok">
            <label className="form-label">Name</label>
            <input
              type="text"
              className="form-control"
              placeholder="Enter your name..."
              {...register("name", { required: true })}
            />
            {errors.name?.type === "required" && "name is required"}
          </div>
          <div className="mb-3">
            <label className="form-label">Email address</label>
            <input
              type="email"
              className="form-control"
              placeholder="Enter your email..."
              aria-describedby="emailHelp"
              {...register("email", { required: true })}
            />
            {errors.email?.type === "required" && "email is required"}
          </div>
          <div className="mb-3">
            <label className="form-label">Phone</label>
            <input
              type="number"
              className="form-control"
              placeholder="Enter your phone..."
              {...register("phone", {
                required: true,
                minLength: 11,
                maxLength: 12,
              })}
            />
            {errors.phone?.type === "required" && "phone is required"}
            {errors.phone?.type === "minLength" &&
              "phone number should be at least 11 digits"}
            {errors.phone?.type === "maxLength" &&
              "phone number should be at most 12 digits"}
          </div>
          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter your password..."
              {...register("password", {
                required: true,
                pattern: /^.*[a-zA-Z].*[@!_-].*[0-9]$/,
              })}
            />
            {errors.password?.type === "validate" && "passwords doesn't match!"}
            {errors.password?.type === "required" && "password is required"}
            {errors.password?.type === "pattern" &&
              "password must be in this syntax: (letters captial or small)(special charaters @!_-)(numbers) in example : XYZ_123"}
          </div>
          <div className="mb-3">
            <label className="form-label">Confirm Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Re-enter your password..."
              {...register("repassword", {
                required: true,
                validate: (val) => {
                  if (watch("password") !== val) {
                    return "password does not match!";
                  }
                },
              })}
            />
            {errors.repassword?.type === "required" && "password is required"}
            {errors.repassword?.type === "validate" &&
              "password does not match!"}
          </div>
          <label className="form-check-label pe-3">Gender</label>
          <div className="form-check form-check-inline">
            <label className="form-check-label">Male</label>
            <input
              className="form-check-input"
              type="radio"
              name="inlineRadioOptions"
              id="inlineRadio1"
              value="Male"
              {...register("gender", { required: true })}
            />
          </div>
          <div className="form-check form-check-inline">
            <label className="form-check-label">Female</label>
            <input
              className="form-check-input"
              type="radio"
              name="inlineRadioOptions"
              id="inlineRadio2"
              value="Female"
              {...register("gender", { required: true })}
            />

            {errors.gender?.type === "required" && " gender is required"}
          </div>
          <br />
          <br />
          <button type="submit" className="btn btn-warning">
            Sign up
          </button>
        </form>
      </div>
      </div>
    
  );
}

export default Signup;
