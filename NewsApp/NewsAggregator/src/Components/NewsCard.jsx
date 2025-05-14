import React from 'react';

const NewsCard = ({ title, link }) => {
  return (
    <div style={{ border: '1px solid #ddd', borderRadius: '8px', padding: '1rem', marginBottom: '1rem' }}>
      <a href={link} target="_blank" rel="noopener noreferrer">{title}</a>
    </div>
  );
};

export default NewsCard;