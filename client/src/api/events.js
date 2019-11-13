import axios from 'axios'
import * as Constants from './constants'

export const fetchEvents = () => {
  return axios.get(Constants.EVENT_URL)
}

export const createEvent = (title, eventStart, eventEnd) => {
  return axios.get(Constants.EVENT_URL, {title, eventStart, eventEnd})
}
