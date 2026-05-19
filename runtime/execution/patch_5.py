javascript
// patches/PATCH_01/api.js
import axios from 'axios';
const API = () => {
  const instance = axios.create({
    baseURL: 'https://api.example.com'
  });
  return instance;
};
export default API;