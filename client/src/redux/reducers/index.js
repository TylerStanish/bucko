import {combineReducers} from 'redux';
import {connectRouter} from 'connected-react-router'

import authReducer from './authReducer'
import eventsReducer from './eventsReducer';

export default history => combineReducers({
  router: connectRouter(history),
  auth: authReducer,
  events: eventsReducer
})