import React from 'react';

const Articles = ({ articles }) => {
  return (
    <div className="articles">
      {articles.length > 0 ? (
        articles.map((article, index) => (
          <div key={index} className="article">
            <h2>{article.title}</h2>
            <p>{article.category}</p>
            <a href={article.link} target="_blank" rel="noopener noreferrer">Read more</a>
            <p>{new Date(article.created_at).toLocaleString()}</p>
          </div>
        ))
      ) : (
        <p></p>
      )}
    </div>
  );
};

export default Articles;