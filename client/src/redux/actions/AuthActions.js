import axios from 'axios'

import * as Types from './Types'

export const getTokenFromLocalStorage = () => {
  return async (dispatch) => {
    const token = await localStorage.getItem('token')
    if (token) {
      dispatch(setToken(token))
      axios.defaults.headers.common['AUTHORIZATION'] = `Bearer ${token}`
    } else {
      dispatch(setToken(''))
      axios.defaults.headers.common['AUTHORIZATION'] = ''
    }
  }
}

export const setToken = token => {
  return {
    type: Types.SET_TOKEN,
    payload: token
  }
}