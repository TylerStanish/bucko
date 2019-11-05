import React from 'react'
import {Calendar, momentLocalizer} from 'react-big-calendar'
import 'react-big-calendar/lib/css/react-big-calendar.css'
import moment from 'moment'
import {connect} from 'react-redux'

const localizer = momentLocalizer(moment)

const DashboardPage = props => {
  return (
    <div>
      <section>
        <Calendar
          localizer={localizer}
          events={props.events}
          startAccessor='start'
          endAccessor='end'
          titleAccessor='title'
          defaultView='day'
          views={['week', 'day', 'agenda']}
        />
      </section>
    </div>
  )
}

export default connect(props => {
  return {
    events: props.events.events
  }
})(DashboardPage)
