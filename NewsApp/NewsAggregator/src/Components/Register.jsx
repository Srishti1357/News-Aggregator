// import React, { useState } from "react";
// import axios from "axios";
// import { useNavigate } from "react-router-dom";
// import './Register.css'

// const Register = () => {
//   const [formData, setFormData] = useState({
//     username: "",
//     password: "",
//   });

//   const [message, setMessage] = useState("");
//   const [error, setError] = useState("");
//   const navigate = useNavigate(); // Initialize the useNavigate hook
//   const [consfirmPsswd, SetConfirmPsswd] = useState("")

//   const handleChange = (e) => {
//     const { name, value } = e.target;
//     setFormData({
//       ...formData,
//       [name]: value,
//     });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     setMessage("");
//     setError("");

//     if (formData.password !== confirmPassword) {
//       setError("Passwords do not match.");
//       return;
//     }

//     try {
//       const response = await axios.post("http://127.0.0.1:8000/register/", formData);
//       setMessage(response.data.message);
//       setFormData({ username: "", password: "" }); // Clear the form

//       // Wait for 2 seconds and navigate to the login page
//       setTimeout(() => {
//         navigate("/login");
//       }, 2000);
//     } catch (error) {
//       if (error.response && error.response.data) {
//         setError(error.response.data.error);
//       } else {
//         setError("Something went wrong. Please try again.");
//       }
//     }
//   };

//   return (
//     <div className="register-container">
//       <h2>Register</h2>
//       <form onSubmit={handleSubmit}>
//         <div className="form-group">
//           <label>Username:</label>
//           <input
//             type="text"
//             name="username"
//             value={formData.username}
//             onChange={handleChange}
//             required
//           />
//         </div>
//         <div className="form-group">
//           <label>Password:</label>
//           <input
//             type="password"
//             name="password"
//             value={formData.password}
//             onChange={handleChange}
//             required
//           />
//         </div>
//         <div className="form-group">
//           <label>Confirm Password:</label>
//           <input
//             type="password"
//             name="confirmPassword"
//             value={SetConfirmPsswd}
//             onChange={handleChange}
//             required
//           />
//         </div>
//         <button type="submit">Register</button>
//       </form>
//       {message && <p className="alert alert-success">{message}</p>}
//       {error && <p className="alert alert-danger">{error}</p>}
//     </div>
//   );
// };

// export default Register;



import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import './Register.css'

const Register = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  const [confirmPassword, setConfirmPassword] = useState(""); // Add separate state for confirmPassword
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate(); // Initialize the useNavigate hook

  const handleChange = (e) => {
    const { name, value } = e.target;

    if (name === "confirmPassword") {
      setConfirmPassword(value); // Update confirmPassword state
    } else {
      setFormData({
        ...formData,
        [name]: value, // Update formData with username and password
      });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");
    setError("");

    // Frontend validation: Check if password and confirmPassword match
    if (formData.password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    // Send only username and password to backend
    try {
      const response = await axios.post("http://127.0.0.1:8000/register/", formData);
      setMessage(response.data.message);
      setFormData({ username: "", password: "" }); // Clear the form
      setConfirmPassword(""); // Clear confirmPassword field

      // Wait for 2 seconds and navigate to the login page
      setTimeout(() => {
        navigate("/login");
      }, 2000);
    } catch (error) {
      if (error.response && error.response.data) {
        setError(error.response.data.error);
      } else {
        setError("Something went wrong. Please try again.");
      }
    }
  };

  return (
    <div className="register-container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Username:</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Confirm Password:</label>
          <input
            type="password"
            name="confirmPassword"
            value={confirmPassword} // Use confirmPassword state for this field
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Register</button>
      </form>
      {message && <p className="alert alert-success">{message}</p>}
      {error && <p className="alert alert-danger">{error}</p>}
    </div>
  );
};

export default Register;
