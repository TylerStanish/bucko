import React from 'react'
import {
  Button,
  Intent
} from '@blueprintjs/core'
import {Calendar, momentLocalizer} from 'react-big-calendar'
import 'react-big-calendar/lib/css/react-big-calendar.css'
import moment from 'moment'
import {connect} from 'react-redux'


import Actions from '../redux/actions'

const localizer = momentLocalizer(moment)

class DashboardPage extends React.Component {
  componentDidMount() {
    this.props.fetchEvents()
  }
  render() {
    return (
      <div>
        <Button
          fill
          text='Add event'
          intent={Intent.PRIMARY}
        />
        <section>
          <Calendar
            localizer={localizer}
            events={this.props.events}
            startAccessor='eventStart'
            endAccessor='eventEnd'
            titleAccessor='title'
            defaultView='day'
            views={['week', 'day', 'agenda']}
          />
        </section>
      </div>
    )
  }
}

export default connect(props => {
  return {
    events: props.events.events
  }
}, {fetchEvents: Actions.events.fetchEvents})(DashboardPage)
