import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { registerUser, fetchRegions } from '../api';

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [regionId, setRegionId] = useState(1); // Default or fetched from API
  const [error, setError] = useState('');
  const [regions, setRegions] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const getRegions = async () => {
      try {
        const data = await fetchRegions();
        setRegions(data);
        // Set default region ID to the first region's ID
        if (data.length > 0) {
          setRegionId(data[0].id);
        }
      } catch (err) {
        console.error('Failed to fetch regions', err);
      }
    };
    getRegions();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await registerUser(username, password, regionId);
      navigate('/');
    } catch (err) {
      setError('Registration failed');
    }
  };

  return (
    <div className="container">
      <h2>Register</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label><br />
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
        </div>
        <div>
          <label>Password:</label><br />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        </div>
        <div>
          <label>Region:</label><br />
          <select value={regionId} onChange={(e) => setRegionId(e.target.value)} required>
            {regions.map((region) => (
              <option key={region.id} value={region.id}>{region.name}</option>
            ))}
          </select>
        </div><br />
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;
