import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [sentence, setSentence] = useState("Waiting for a sentence...");
  const [paragraph, setParagraph] = useState("Waiting for a paragraph...");

  const fetchAll = () => {
    fetch('http://localhost:8095/api/last-sentence')
      .then((res) => res.json())
      .then((data) => { if (data.sentence) setSentence(data.sentence); })
      .catch(() => setSentence("Could not connect to API"));

    fetch('http://localhost:8095/api/last-paragraph')
      .then((res) => res.json())
      .then((data) => { if (data.paragraph) setParagraph(data.paragraph); })
      .catch(() => setParagraph("Could not connect to API"));
  };

  useEffect(() => {
    fetchAll();
    const interval = setInterval(fetchAll, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Latest Paragraph Service</h1>
        <div className="sentence-card">
          <p>"{sentence}"</p>
          <p>"{paragraph}"</p>
        </div>
        <button onClick={fetchAll} className="refresh-button">
          Refresh Now
        </button>
      </header>
    </div>
  );
}

export default App;