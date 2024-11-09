import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Your FastAPI backend URL

const axiosInstance = axios.create({
  baseURL: API_URL,
});

export const setAuthToken = (token) => {
  if (token) {
    axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete axiosInstance.defaults.headers.common['Authorization'];
  }
};

export const fetchRegions = async () => {
  const response = await axiosInstance.get('/regions/');
  return response.data;
};


export const loginUser = async (username, password) => {
  const response = await axiosInstance.post('/token', new URLSearchParams({
    username,
    password,
  }));
  return response.data;
};

export const fetchCurrentQuestion = async () => {
  const response = await axiosInstance.get('/question/');
  return response.data;
};

export const registerUser = async (username, password, region_id) => {
  const response = await axiosInstance.post('/users/', {
    username,
    password,
    region_id,
  });
  return response.data;
};


export default axiosInstance;
