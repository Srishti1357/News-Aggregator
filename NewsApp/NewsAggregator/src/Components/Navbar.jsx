

import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Navbar.css';

const Navbar = () => {
  const navigate = useNavigate();
  const isLoggedIn = Boolean(sessionStorage.getItem('accessToken'));
  const username = sessionStorage.getItem('username');
  const [searchQuery, setSearchQuery] = useState('');

  const handleLogout = async () => {
    const refreshToken = sessionStorage.getItem('refreshToken');

    try {
      await axios.post('https://django-backend-7mwp.onrender.com/logout/', { refresh: refreshToken }, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${sessionStorage.getItem('accessToken')}`,
        },
      });

      sessionStorage.clear();
      localStorage.removeItem('username');
      navigate('/login');
    } catch (error) {
      console.error('Error during logout:', error);
    }
  };

  const handleSearchChange = (e) => setSearchQuery(e.target.value);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/?search=${searchQuery}`);
    }
  };

  return (
    <nav className="navbar fixed-top navbar-expand">
      <div className="navbar-section left">
        <Link to="/" className="brand">News Aggregator</Link>
      </div>

      <div className="navbar-section center">
        {isLoggedIn ? (
          <form className="search-form" onSubmit={handleSearchSubmit}>
            <input
              type="text"
              placeholder="Search articles..."
              value={searchQuery}
              onChange={handleSearchChange}
            />
            <button type="submit">Search</button>
          </form>
        ) : (
          <div className="empty-placeholder" />
        )}
      </div>

      <div className="navbar-section right">
        {isLoggedIn ? (
          <>
            <Link to="/" className="nav-link-basic">Home</Link>
            <Link to="/saved" className="nav-link-basic">Saved</Link>
            <span className="username">Hi, {username}</span>
            <button className="logout-button" onClick={handleLogout}>Logout</button>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
