import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  // 1. "State" is like a variable that React watches. 
  // When 'sentence' changes, the screen updates automatically.
  const [sentence, setSentence] = useState("Waiting for a sentence...");

  // 2. This function calls your FastAPI
  const fetchLatestSentence = () => {
    fetch('http://localhost:8095/api/last-sentence')
      .then((response) => response.json())
      .then((data) => {
        // If the API returned a sentence, save it to our state
        if (data.sentence) {
          setSentence(data.sentence);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setSentence("Could not connect to API");
      });
  };

  // 3. "useEffect" runs once when the component first appears on the screen
  useEffect(() => {
    fetchLatestSentence();

    // Optional: Refresh every 5 seconds so you see new sentences automatically
    const interval = setInterval(fetchLatestSentence, 5000);
    return () => clearInterval(interval); // Clean up when the page closes
  }, []);

  // 4. This is what actually gets drawn in the browser (HTML-like syntax)
  return (
    <div className="App">
      <header className="App-header">
        <h1>Latest Paragraph Service</h1>
        <div className="sentence-card">
          <p>"{sentence}"</p>
        </div>
        <button onClick={fetchLatestSentence} className="refresh-button">
          Refresh Now
        </button>
      </header>
    </div>
  );
}

export default App;
