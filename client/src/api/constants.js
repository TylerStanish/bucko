// export const BASE_URL = '/api/'
// export const BASE_URL = 'http://localhost:5000/api/'
export const BASE_URL = process.env.REACT_APP_API_URL
export const LOGIN_URL = BASE_URL + 'auth/login/'
export const SIGNUP_URL = BASE_URL + 'auth/signup/'
export const EVENT_URL = BASE_URL + 'event/'
