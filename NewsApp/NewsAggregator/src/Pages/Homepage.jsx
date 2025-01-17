import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Homepage.css'; // Import the CSS file

const Homepage = () => {
  const [articles, setArticles] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const token = sessionStorage.getItem('accessToken');
    if (!token) {
      navigate('/login');
      return;
    }

    axios
      .get('http://127.0.0.1:8000/articles/', {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      })
      .then((response) => {
        setArticles(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error('Error fetching articles:', error);
      });
  }, [navigate]);

  return (
    <div className=" mt-4 homepage">
      <h2>Top Headlines</h2>
      {articles.length === 0 ? (
        <p className="loading">Loading...</p>
      ) : (
        <div className="article-list">
          {articles.map((article, index) => (
            <div key={index} className="article">
              <h4>{article.title}</h4>
              {article.publisher_logo && (
                <img src={article.publisher_logo} alt="Publisher" />
              )}
              <a href={article.link} target="_blank" rel="noopener noreferrer">
                Read More
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Homepage;