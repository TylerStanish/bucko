import axios from 'axios'
import {push} from 'connected-react-router'

import * as Types from './Types'
import Actions from './'
import Api from '../../api'

export const getTokenFromLocalStorage = () => {
  return async dispatch => {
    const token = await localStorage.getItem('token')
    // axios.defaults.headers.common['Content-Type'] = 'application/json'
    if (token) {
      console.log(token)
      dispatch(setToken(token))
      axios.defaults.headers.common['AUTHORIZATION'] = `Bearer ${token}`
      dispatch(Actions.events.fetchEvents())
    } else {
      dispatch(setToken(''))
      axios.defaults.headers.common['AUTHORIZATION'] = ''
    }
  }
}

export const setToken = token => {
  return async dispatch => {
    await localStorage.setItem('token', token)
    axios.defaults.headers.common['AUTHORIZATION'] = `Bearer ${token}`
    dispatch({
      type: Types.SET_TOKEN,
      payload: token
    })
  }
}

export const login = (email, password) => {
  return async dispatch => {
    const res = await Api.auth.login(email, password)
    const {token} = res.data
    dispatch(setToken(token))
    dispatch(push('/dashboard'))
  }
}

export const logout = () => {
  return async dispatch => {
    dispatch(setToken(''))
    dispatch(push('/'))
  }
}

export const signup = (email, password) => {
  return async dispatch => {
    const res = await Api.auth.signup(email, password)
    const {token} = res.data
    dispatch(setToken(token))
    dispatch(push('/dashboard'))
  }
}
