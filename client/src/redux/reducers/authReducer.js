import * as Types from '../actions/Types'

const initialState = {
  loginLoading: false,
  loginError: '',
  token: '',
  signupLoading: false,
}

export default (state = initialState, action) => {
  switch(action.type) {
    case Types.SET_TOKEN:
      return {
        ...state,
        token: action.payload
      }
    case Types.LOGIN_LOADING:
      return {
        ...state,
        loginLoading: action.payload
      }
    case Types.SIGNUP_LOADING:
      return {
        ...state,
        signupLoading: action.payload
      }
    default:
      return state
  }
}
