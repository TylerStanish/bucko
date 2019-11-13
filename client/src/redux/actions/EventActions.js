import axios from 'axios'

import Api from '../../api'
import * as Types from './Types.js'


export const fetchEvents = () => {
  return async (dispatch, getState) => {
    console.log(getState())
    const res = await Api.events.fetchEvents()
    res.data = res.data.map(event => ({
      ...event,
      eventStart: new Date(event.eventStart),
      eventEnd: new Date(event.eventEnd),
    }))
    dispatch({
      type: Types.FETCH_EVENTS,
      payload: res.data
    })
  }
}
