import moment from 'moment'
import * as Types from '../actions/Types'

const initialState = {
  events: [
    {
      title: 'do this thing',
      start: moment(new Date())._d,
      end: moment(new Date(Date.now() + 1000*60*60))._d
    }
  ]
}

export default (state = initialState, action) => {
  switch(action.type) {
    case Types.FETCH_EVENTS:
      return {
        ...state,
        events: action.payload
      }
    default:
      return initialState
  }
}
