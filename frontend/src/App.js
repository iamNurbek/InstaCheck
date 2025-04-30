import React, { useState } from 'react';
import './App.css';

function App() {
  const [followers, setFollowers] = useState('');
  const [following, setFollowing] = useState('');
  const [result, setResult] = useState([]);

  const compareFollow = async () => {
    try {
      const response = await fetch('https://instacheck.onrender.com/compare', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          followers: followers,
          following: following,
        }),
      });

      const data = await response.json();
      setResult(data.not_following_back);
    } catch (error) {
      console.error('Error:', error);
      alert('Something went wrong. Is the backend running?');
    }
  };

  return (
    <div className="App">
      <h1>InstaCheck</h1>

      <div className="input-container">
        <div>
          <h2>Your Followers</h2>
          <textarea
            rows={10}
            cols={40}
            value={followers}
            onChange={(e) => setFollowers(e.target.value)}
          />
        </div>

        <div>
          <h2>Your Following</h2>
          <textarea
            rows={10}
            cols={40}
            value={following}
            onChange={(e) => setFollowing(e.target.value)}
          />
        </div>
      </div>

      <button onClick={compareFollow}>Submit</button>

      {result.length > 0 && (
        <div>
          <h2>Not Following You Back</h2>
          <ul>
            {result.map((user, idx) => (
              <li key={idx}>
                <a
                  href={`https://www.instagram.com/${user}`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {user}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
