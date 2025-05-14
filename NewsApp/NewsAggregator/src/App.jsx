import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './Components/Navbar';
import Homepage from './Pages/Homepage';
import Login from './Components/Login';
import Register from './Components/Register';
import SavedArticles from './Pages/SavedArticles';
import CategoryFilter from './Pages/CategoryFilter';
// import './App.css';

const App = () => {
  return (
    <Router>
      <Navbar />
      <div style={{ padding: '4rem' }}>
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/saved" element={<SavedArticles />} />
          <Route path="/category/:category" element={<CategoryFilter />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;