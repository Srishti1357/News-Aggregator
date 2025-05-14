

import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useLocation } from "react-router-dom";
import CategoryFilter from "./CategoryFilter";
import "./SavedArticles.css";

const SavedArticles = () => {
  const [articles, setArticles] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("");

  const fetchSavedArticles = () => {
    const token = sessionStorage.getItem("accessToken");
    axios
      .get("http://127.0.0.1:8000/saved-articles/", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        setArticles(response.data);
      })
      .catch((error) => {
        console.error("Error fetching saved articles:", error);
      });
  };

  const removeSavedArticle = (articleId) => {
    const token = sessionStorage.getItem("accessToken");
    axios
      .delete(`http://127.0.0.1:8000/remove-saved-article/${articleId}/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(() => {
        setArticles((prevArticles) =>
          prevArticles.filter((article) => article.id !== articleId)
        );
      })
      .catch((error) => {
        console.error("Error removing saved article:", error);
      });
  };

  useEffect(() => {
    fetchSavedArticles();
  }, []);

  return (
    <div className="mt-4 saved-homepage">
      <br></br>
      <h2 className="saved-headline">Saved Headlines</h2>

      {articles.length > 0 ? (
        <div className="saved-article-list">
          {articles.map((article, index) => (
            <div key={index} className="saved-article">
              {article.image !== "None" ? (
                <img src={article.image} alt="Article" className="saved-imageUrl" />
              ) : article.video ? (
                <video controls className="saved-video-player">
                  <source src={article.video} type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
              ) : (
                <p className="text-gray-400">No Media Available</p>
              )}

              <h4 title={article.title}>{article.title}</h4>

              {article.publisher_logo && (
                <img
                  src={article.publisher_logo}
                  alt="Publisher"
                  className="saved-publisher-logo"
                />
              )}

              <a href={article.link} target="_blank" rel="noopener noreferrer">
                Read More
              </a>

              <button onClick={() => removeSavedArticle(article.id)} className="saved-remove-button">
                Remove
              </button>
            </div>
          ))}
        </div>
      ) : (
        <p>No saved articles.</p>
      )}
    </div>
  );
};

export default SavedArticles;
