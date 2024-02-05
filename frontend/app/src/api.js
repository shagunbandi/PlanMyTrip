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

    // Check if the request is for 'multipart/form-data'

    console.log(config.data)
    if (config.headers['Content-Type'] === 'multipart/form-data') {
      // Use FormData for file uploads
      config.data = convertObjectToFormData(config.data)
    }

    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)

// Helper function to convert an object to FormData
function convertObjectToFormData(object) {
  const formData = new FormData()

  Object.keys(object).forEach((key) => {
    formData.append(key, object[key])
  })

  return formData
}

export default api
