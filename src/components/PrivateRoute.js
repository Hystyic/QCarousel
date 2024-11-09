import React, { useEffect, useState } from 'react';
import { fetchCurrentQuestion } from '../api';

const Question = () => {
  const [question, setQuestion] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const getQuestion = async () => {
      try {
        const data = await fetchCurrentQuestion();
        setQuestion(data);
      } catch (err) {
        setError('Failed to fetch question');
      }
    };
    getQuestion();
  }, []);

  if (error) {
    return <p style={{ color: 'red' }}>{error}</p>;
  }

  if (!question) {
    return <p>Loading...</p>;
  }

  return (
    <div className="container">
      <h2>Current Question</h2>
      <p>{question.content}</p>
    </div>
  );
};

export default Question;
