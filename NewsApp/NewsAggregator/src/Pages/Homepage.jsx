import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useLocation } from "react-router-dom";
import "./Homepage.css"; // Import the CSS file

const Homepage = () => {
  const [articles, setArticles] = useState([]);
  const navigate = useNavigate();
  const location = useLocation();
  const searchQuery = new URLSearchParams(location.search).get("search"); // Extract search query from URL


  const formatDate = (isoString) => {
    if (!isoString) return "Unknown Date"; // Handle null/undefined cases
  
    const date = new Date(isoString);
  
    // Format date as "February 7, 2025"
    const formattedDate = date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  
    // Format time as "01:16:12 PM"
    const formattedTime = date.toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: true, // Ensures AM/PM format
    });
  
    return `${formattedDate}  ${formattedTime}`; // Combine date and time
  };
  

  useEffect(() => {
    const token = sessionStorage.getItem("accessToken");
    if (!token) {
      navigate("/login");
      return;
    }

    const fetchArticles = () => {
      let url = "http://127.0.0.1:8000/articles/"; // Default URL

      // If there's a search query, append it to the URL
      if (searchQuery) {
        url = `http://127.0.0.1:8000/articles/?search=${searchQuery}`;
      }

      axios
        .get(url, {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          setArticles(response.data);
        })
        .catch((error) => {
          console.error("Error fetching articles:", error);
        });
    };

    fetchArticles(); // Call the function to fetch articles based on search query
  }, [navigate, searchQuery]); // Trigger effect on searchQuery change

  return (
    <div className="mt-4 homepage">
      <h2>Top Headlines</h2>
      {articles.length === 0 ? (
        <p className="loading">Loading...</p>
      ) : (
        <div className="article-list">
          {articles.map((article, index) => (
            <div key={index} className="article">
              {article.image != "None" ? (
                <img
                  src={article.image}
                  alt="Article"
                  className = "imageUrl"
                />
              ) : article.video ? (
                <video controls className="video-player">
                  <source src={article.video} type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
              ) : (
                <p className="text-gray-400">No Media Available</p>
              )}
              <h4>{article.title}</h4>
              <p>{formatDate(article.lastmod)}</p>
              {article.publisher_logo && (
                <img src={article.publisher_logo} alt="Publisher" className="publisher-logo" />
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
