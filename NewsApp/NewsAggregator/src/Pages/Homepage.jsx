
// import React, { useEffect, useState, useRef } from "react";
// import axios from "axios";
// import { useNavigate, useLocation } from "react-router-dom";
// import { ClipLoader } from "react-spinners"; // Import the spinner
// import "./Homepage.css"; // Import CSS file
// import CategoryFilter from "./CategoryFilter"; // Import CategoryFilter component

// const Homepage = () => {
//   const [articles, setArticles] = useState([]);
//   const [savedArticles, setSavedArticles] = useState([]);
//   const [loading, setLoading] = useState(true); // Track loading state for initial fetch
//   const [loadingMore, setLoadingMore] = useState(false); // Track loading state for "Load More"
//   const [page, setPage] = useState(1); // Track the current page
//   const [hasMore, setHasMore] = useState(true); // Track if more pages are available
//   const navigate = useNavigate();
//   const location = useLocation();
//   const searchQuery = new URLSearchParams(location.search).get("search");
//   const observerRef = useRef(null); // Reference for intersection observer

//   const [selectedCategory, setSelectedCategory] = useState(""); // Add this

//   const formatDate = (isoString) => {
//     if (!isoString) return "Unknown Date";

//     const date = new Date(isoString);

//     const formattedDate = date.toLocaleDateString("en-US", {
//       year: "numeric",
//       month: "long",
//       day: "numeric",
//     });

//     const formattedTime = date.toLocaleTimeString("en-US", {
//       hour: "2-digit",
//       minute: "2-digit",
//       second: "2-digit",
//       hour12: true,
//     });

//     return `${formattedDate}  ${formattedTime}`;
//   };

//   useEffect(() => {
//     const token = sessionStorage.getItem("accessToken");
//     if (!token) {
//       navigate("/login");
//       return;
//     }

//     const fetchArticles = () => {
//       setLoading(page === 1); // Show loading spinner only for initial load
//       setHasMore(true); // Reset the 'hasMore' flag on new search or filter

//       let url = `http://127.0.0.1:8000/articles/?page=${page}`;

//       if (searchQuery) {
//         url += `&search=${searchQuery}`;
//       }

//       if (selectedCategory) {
//         url = `http://127.0.0.1:8000//articles/filter/?category=${selectedCategory}`;
//       }

//       axios
//         .get(url, {
//           headers: {
//             "Content-Type": "application/json",
//             Authorization: `Bearer ${token}`,
//           },
//         })
//         .then((response) => {
//           const newArticles = response.data.results || response.data;

//           if (newArticles.length === 0 || newArticles.length < 10) {
//             setHasMore(false);
//           }

//           setTimeout(() => {
//             // 🔥 Fix: Append articles if page > 1, otherwise replace
//             setArticles((prevArticles) =>
//               page === 1 ? newArticles : [...prevArticles, ...newArticles]
//             );
//             setLoading(false);
//             setLoadingMore(false);
//           }, 2000);
//         })
//         .catch((error) => {
//           console.error("Error fetching articles:", error.response || error);
//           setLoading(false);
//           setLoadingMore(false);
//         });
//     };

//     const fetchSavedArticles = () => {
//       axios
//         .get("http://127.0.0.1:8000/saved-articles/", {
//           headers: {
//             "Content-Type": "application/json",
//             Authorization: `Bearer ${token}`,
//           },
//         })
//         .then((response) => {
//           setSavedArticles(response.data.map((article) => article.id));
//         })
//         .catch((error) => {
//           console.error("Error fetching saved articles:", error.response || error);
//         });
//     };

//     fetchArticles();
//     fetchSavedArticles();
//   }, [navigate, searchQuery, page, selectedCategory]);

//   const handleSaveArticle = (articleId) => {
//     const token = sessionStorage.getItem("accessToken");
//     axios
//       .post(
//         `http://127.0.0.1:8000/save-article/${articleId}/`,
//         {},
//         {
//           headers: {
//             "Content-Type": "application/json",
//             Authorization: `Bearer ${token}`,
//           },
//         }
//       )
//       .then(() => {
//         setSavedArticles((prev) => [...prev, articleId]);
//       })
//       .catch((error) => {
//         console.error("Error saving article:", error.response || error);
//       });
//   };

//   const loadMoreArticles = () => {
//     if (hasMore && !loadingMore) {
//       setLoadingMore(true);
//       setPage((prevPage) => prevPage + 1);
//     }
//   };

//   // Intersection Observer logic
//   useEffect(() => {
//     const observer = new IntersectionObserver(
//       (entries) => {
//         const first = entries[0];
//         if (first.isIntersecting && !loading && !loadingMore && hasMore) {
//           loadMoreArticles();
//         }
//       },
//       { threshold: 1.0 }
//     );

//     if (observerRef.current) {
//       observer.observe(observerRef.current);
//     }

//     return () => {
//       if (observerRef.current) {
//         observer.unobserve(observerRef.current);
//       }
//     };
//   }, [loading, loadingMore, hasMore]);

//   return (
//     <div className="mt-4 homepage">
//       <CategoryFilter
//         categories={[
//           "home",
//           "business",
//           "entertainment",
//           "sports",
//           "technology",
//           "politics",
//         ]}
//         selectedCategory={selectedCategory}
//         setSelectedCategory={setSelectedCategory}
//       />

//       <h2>Top Headlines</h2>

//       {loading && articles.length === 0 ? (
//         <div className="loading-message">
//           <ClipLoader color="#3498db" loading={true} size={50} />
//           <p>Loading...</p>
//         </div>
//       ) : (
//         <div className="article-list">
//           {articles.map((article, index) => (
//             <div key={index} className="article">
//               {article.image !== "None" ? (
//                 <img src={article.image} alt="Article" className="imageUrl" />
//               ) : article.video ? (
//                 <video controls className="video-player">
//                   <source src={article.video} type="video/mp4" />
//                   Your browser does not support the video tag.
//                 </video>
//               ) : (
//                 <p className="text-gray-400">No Media Available</p>
//               )}
//               {/* <h4>{article.title}</h4> */}
//               <h4 title={article.title}>{article.title}</h4>

//               <p>{formatDate(article.lastmod)}</p>
//               {article.publisher_logo && (
//                 <img
//                   src={article.publisher_logo}
//                   alt="Publisher"
//                   className="publisher-logo"
//                 />
//               )}
//               <a href={article.link} target="_blank" rel="noopener noreferrer">
//                 Read More
//               </a>
//               {savedArticles.includes(article.id) ? (
//                 <p style={{ color: "green", fontWeight: "bold" }}>
//                   Saved Article
//                 </p>
//               ) : (
//                 <button onClick={() => handleSaveArticle(article.id)}>
//                   Save Article
//                 </button>
//               )}
//             </div>
//           ))}
//         </div>
//       )}

//       {loadingMore && (
//         <div className="loading-message">
//           <ClipLoader color="#3498db" loading={true} size={50} />
//           <p>Loading more articles...</p>
//         </div>
//       )}

//       {!hasMore && !loading && (
//         <p className="no-more-articles">No more articles to show</p>
//       )}

//       <div ref={observerRef}></div>
//     </div>
//   );
// };

// export default Homepage;



import React, { useEffect, useState, useRef } from "react";
import axios from "axios";
import { useNavigate, useLocation } from "react-router-dom";
import { ClipLoader } from "react-spinners"; // Spinner
import "./Homepage.css";
import CategoryFilter from "./CategoryFilter";

const Homepage = () => {
  const [articles, setArticles] = useState([]);
  const [savedArticles, setSavedArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [loadingMore, setLoadingMore] = useState(false);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState("");
  const navigate = useNavigate();
  const location = useLocation();
  const searchQuery = new URLSearchParams(location.search).get("search");
  const observerRef = useRef(null);

  const formatDate = (isoString) => {
    if (!isoString) return "Unknown Date";
    const date = new Date(isoString);
    const formattedDate = date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    const formattedTime = date.toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: true,
    });
    return `${formattedDate}  ${formattedTime}`;
  };

  useEffect(() => {
    const token = sessionStorage.getItem("accessToken");
    if (!token) {
      navigate("/login");
      return;
    }

    const fetchArticles = () => {
      setLoading(page === 1);
      setHasMore(true);

      let url = `http://127.0.0.1:8000/articles/?page=${page}`;
      if (searchQuery) {
        url += `&search=${searchQuery}`;
      }
      if (selectedCategory) {
        url = `http://127.0.0.1:8000/articles/filter/?category=${selectedCategory}&page=${page}`;
        if (searchQuery) {
          url += `&search=${searchQuery}`;
        }
      }

      axios
        .get(url, {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          const newArticles = response.data.results || response.data;

          // ✅ Use .next to determine if more pages exist
          if (!response.data.next) {
            setHasMore(false);
          }

          setTimeout(() => {
            setArticles((prevArticles) =>
              page === 1 ? newArticles : [...prevArticles, ...newArticles]
            );
            setLoading(false);
            setLoadingMore(false);
          }, 2000);
        })
        .catch((error) => {
          console.error("Error fetching articles:", error.response || error);
          setLoading(false);
          setLoadingMore(false);
          setHasMore(false); // Prevent infinite loading on error
        });
    };

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
          setSavedArticles(response.data.map((article) => article.id));
        })
        .catch((error) => {
          console.error("Error fetching saved articles:", error.response || error);
        });
    };

    fetchArticles();
    fetchSavedArticles();
  }, [navigate, searchQuery, page, selectedCategory]);

  const handleSaveArticle = (articleId) => {
    const token = sessionStorage.getItem("accessToken");
    axios
      .post(
        `http://127.0.0.1:8000/save-article/${articleId}/`,
        {},
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        }
      )
      .then(() => {
        setSavedArticles((prev) => [...prev, articleId]);
      })
      .catch((error) => {
        console.error("Error saving article:", error.response || error);
      });
  };

  const loadMoreArticles = () => {
    if (hasMore && !loadingMore) {
      setLoadingMore(true);
      setPage((prevPage) => prevPage + 1);
    }
  };

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        const first = entries[0];
        if (first.isIntersecting && !loading && !loadingMore && hasMore) {
          loadMoreArticles();
        }
      },
      { threshold: 1.0 }
    );

    if (observerRef.current) {
      observer.observe(observerRef.current);
    }

    return () => {
      if (observerRef.current) {
        observer.unobserve(observerRef.current);
      }
    };
  }, [loading, loadingMore, hasMore]);

  return (
    <div className="mt-4 homepage">
      <br></br>
      <CategoryFilter
        categories={[
          "home",
          "business",
          "entertainment",
          "sports",
          "technology",
          "politics",
        ]}
        selectedCategory={selectedCategory}
        setSelectedCategory={(category) => {
          setPage(1); // reset to page 1 on filter change
          setArticles([]); // clear old articles
          setSelectedCategory(category);
        }}
      />

      <h2>Top Headlines</h2>

      {loading && articles.length === 0 ? (
        <div className="loading-message">
          <ClipLoader color="#3498db" loading={true} size={50} />
          <p>Loading...</p>
        </div>
      ) : (
        <div className="article-list">
          {articles.map((article, index) => (
            <div key={index} className="article">
              {article.image !== "None" ? (
                <img src={article.image} alt="Article" className="imageUrl" />
              ) : article.video ? (
                <video controls className="video-player">
                  <source src={article.video} type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
              ) : (
                <p className="text-gray-400">No Media Available</p>
              )}

              <h4 title={article.title}>{article.title}</h4>
              <p>{formatDate(article.lastmod)}</p>

              {article.publisher_logo && (
                <img
                  src={article.publisher_logo}
                  alt="Publisher"
                  className="publisher-logo"
                />
              )}

              <a href={article.link} target="_blank" rel="noopener noreferrer">
                Read More
              </a>

              {savedArticles.includes(article.id) ? (
                <p style={{ color: "green", fontWeight: "bold" }}>
                  Saved Article
                </p>
              ) : (
                <button onClick={() => handleSaveArticle(article.id)}>
                  Save Article
                </button>
              )}
            </div>
          ))}
        </div>
      )}

      {loadingMore && (
        <div className="loading-message">
          <ClipLoader color="#3498db" loading={true} size={50} />
          <p>Loading more articles...</p>
        </div>
      )}

      {!hasMore && !loading && (
        <p className="no-more-articles">🚫 No more articles to show</p>
      )}

      <div ref={observerRef}></div>
    </div>
  );
};

export default Homepage;
