// api.js

import axios from 'axios'

// Create an Axios instance with default values
const api = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Set up an interceptor to add the authorization token from local storage to every request
api.interceptors.request.use(
  (config) => {
    const access = localStorage.getItem('access')
    if (access) {
      config.headers.Authorization = `Bearer ${access}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)

export default api