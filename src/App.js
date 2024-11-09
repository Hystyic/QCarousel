import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { setAuthToken } from './api';
import Login from './components/Login';
import Question from './components/Question';
import PrivateRoute from './components/PrivateRoute';
import Register from './components/Register';


function App() {
  useEffect(() => {
    const token = localStorage.getItem('token');
    setAuthToken(token);
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route
          path="/question"
          element={
            <PrivateRoute>
              <Question />
            </PrivateRoute>
          }
        />
        <Route path="/register" element={<Register />} />

      </Routes>
    </Router>
  );
}

export default App;
