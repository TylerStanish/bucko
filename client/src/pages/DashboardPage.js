import React from 'react'
import {
  Button,
  Classes,
  Dialog,
  Intent,
  Overlay
} from '@blueprintjs/core'
import {Calendar, momentLocalizer} from 'react-big-calendar'
import 'react-big-calendar/lib/css/react-big-calendar.css'
import moment from 'moment'
import {connect} from 'react-redux'
import Actions from '../redux/actions'

import CreateEvent from '../components/modals/CreateEvent'

const localizer = momentLocalizer(moment)


class DashboardPage extends React.Component {
  state = {
    overlayOpen: false
  }
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
          onClick={() => this.setState({overlayOpen: true})}
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
        <Dialog isOpen={this.state.overlayOpen} onClose={() => this.setState({overlayOpen: false})} className={Classes.OVERLAY_SCROLL_CONTAINER}>
          <CreateEvent/>
        </Dialog>
      </div>
    )
  }
}

export default connect(props => {
  return {
    events: props.events.events
  }
}, {fetchEvents: Actions.events.fetchEvents})(DashboardPage)
