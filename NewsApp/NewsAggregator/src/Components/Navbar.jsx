// import React from 'react';
// import { Link, useNavigate } from 'react-router-dom';
// import axios from 'axios';
// import './Navbar.css';

// const Navbar = () => {
//   const navigate = useNavigate();
//   const isLoggedIn = Boolean(sessionStorage.getItem('accessToken'));
//   const username = sessionStorage.getItem('username'); // Handle missing username

//   const handleLogout = async () => {
//     const refreshToken = sessionStorage.getItem('refreshToken');

//     try {
//       await axios.post('http://127.0.0.1:8000/logout/', { refresh: refreshToken }, {
//         headers: {
//           'Content-Type': 'application/json',
//           'Authorization': `Bearer ${sessionStorage.getItem('accessToken')}`
//         },
//       });

//       // Clear tokens and username from storage
//       sessionStorage.removeItem('accessToken');
//       sessionStorage.removeItem('refreshToken');
//       sessionStorage.removeItem('username');
//       localStorage.removeItem('username'); // Optionally clear username from localStorage

//       // Navigate to the login page
//       navigate('/login');
//     } catch (error) {
//       console.error('Error during logout:', error);
//     }
//   };

//   return (
//     <nav className="navbar fixed-top">
//       <ul>
//         <li>
//           <Link to="/">Home</Link>
//         </li>
//         {isLoggedIn ? (
//           <>
//             <li>Hi, {username}</li>
//             <li>
//               <button onClick={handleLogout} className="logout-button">Logout</button>
//             </li>
//           </>
//         ) : (
//           <>
//             <li>
//               <Link to="/login">Login</Link>
//             </li>
//             <li>
//               <Link to="/register">Register</Link>
//             </li>
//           </>
//         )}
//       </ul>
//     </nav>
//   );
// };

// export default Navbar;





import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Navbar.css';

const Navbar = () => {
  const navigate = useNavigate();
  const isLoggedIn = Boolean(sessionStorage.getItem('accessToken'));
  const username = sessionStorage.getItem('username'); // Handle missing username
  const [searchQuery, setSearchQuery] = useState('');

  const handleLogout = async () => {
    const refreshToken = sessionStorage.getItem('refreshToken');

    try {
      await axios.post('http://127.0.0.1:8000/logout/', { refresh: refreshToken }, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${sessionStorage.getItem('accessToken')}`,
        },
      });

      // Clear tokens and username from storage
      sessionStorage.removeItem('accessToken');
      sessionStorage.removeItem('refreshToken');
      sessionStorage.removeItem('username');
      localStorage.removeItem('username'); // Optionally clear username from localStorage

      // Navigate to the login page
      navigate('/login');
    } catch (error) {
      console.error('Error during logout:', error);
    }
  };

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    // Navigate to the Homepage with search query in the URL
    if (searchQuery.trim()) {
      navigate(`/?search=${searchQuery}`);
    }
  };

  return (
    <nav className="navbar fixed-top">
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        {isLoggedIn ? (
          <>
            <li>Hi, {username}</li>
            <li>
              <button onClick={handleLogout} className="logout-button">Logout</button>
            </li>
            {/* Search Box visible only when logged in */}
            <li>
              <form onSubmit={handleSearchSubmit} className="search-form">
                <input
                  type="text"
                  value={searchQuery}
                  onChange={handleSearchChange}
                  placeholder="Search articles..."
                  className="search-input"
                />
                <button type="submit" className="search-button">Search</button>
              </form>
            </li>
          </>
        ) : (
          <>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/register">Register</Link>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
