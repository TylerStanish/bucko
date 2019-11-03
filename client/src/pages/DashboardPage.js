import React from 'react'
import {Calendar, momentLocalizer} from 'react-big-calendar'
import 'react-big-calendar/lib/css/react-big-calendar.css'
import moment from 'moment'

const localizer = momentLocalizer(moment)

export default () => {
  return (
    <div>
      <Calendar
        localizer={localizer}
        events={[]}
      />
    </div>
  )
}