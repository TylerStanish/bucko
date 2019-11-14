import * as Types from '../actions/Types'

const initialState = {
  loginLoading: false,
  loginError: '',
  token: '',
}

export default (state = initialState, action) => {
  switch(action.type) {
    case Types.SET_TOKEN:
      return {
        ...state,
        token: action.payload
      }
    default:
      return state
  }
}
