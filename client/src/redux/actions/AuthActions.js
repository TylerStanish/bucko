import axios from 'axios'

import * as Types from './Types'
import Api from '../../api'

export const getTokenFromLocalStorage = () => {
  return async dispatch => {
    const token = await localStorage.getItem('token')
    console.log('called me!', token)
    // axios.defaults.headers.common['Content-Type'] = 'application/json'
    if (token) {
      dispatch(setToken(token))
      // axios.defaults.headers.common['AUTHORIZATION'] = `Bearer ${token}`
    } else {
      dispatch(setToken(''))
      // axios.defaults.headers.common['AUTHORIZATION'] = ''
    }
  }
}

export const setToken = token => {
  return {
    type: Types.SET_TOKEN,
    payload: token
  }
}

export const login = (email, password) => {
  return async dispatch => {
    const res = await Api.auth.login(email, password)
    console.log('login', res)
  }
}

export const signup = (email, password) => {
  return async dispatch => {
    const res = await Api.auth.signup(email, password)
    console.log('signup', res)
  }
}