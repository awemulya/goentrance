import axios from 'axios'

export default() => {
  return axios.create({
    baseURL: `http://dotag.naxa.com.np/api/`,
    withCredentials: true,
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  })
}
