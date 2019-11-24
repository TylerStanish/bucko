import axios from 'axios'
import * as Constants from './constants'

export const login = (email, password) => {
  return axios.post(Constants.LOGIN_URL, {email, password})
}

export const signup = (email, password) => {
  return axios.post(Constants.SIGNUP_URL, {email, password})
}
