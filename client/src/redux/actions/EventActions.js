import axios from 'axios'
import moment from 'moment'

import Api from '../../api'
import * as Types from './Types.js'


export const fetchEvents = () => {
  return async (dispatch, getState) => {
    console.log(getState())
    const res = await Api.events.fetchEvents()
    res.data = res.data.map(event => ({
      ...event,
      eventStart: moment(event.eventStart).toDate(),
      eventEnd: moment(event.eventEnd).toDate(),
    }))
    dispatch({
      type: Types.FETCH_EVENTS,
      payload: res.data
    })
  }
}

export const createEvent = (title, eventStart, eventEnd) => {
  return async dispatch => {
    const res = await Api.events.createEvent(title, eventStart, eventEnd)
    dispatch(fetchEvents())
  }
}
