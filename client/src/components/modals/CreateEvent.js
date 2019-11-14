import React, {useState} from 'react'
import {InputGroup, Button} from '@blueprintjs/core'
import {
  DateTimePicker
} from '@blueprintjs/datetime'
import { connect } from 'react-redux'

import Actions from '../../redux/actions'


const CreateEvent = props => {
  const [title, setTitle] = useState('')
  const [eventStart, setEventStart] = useState(new Date())
  const [eventEnd, setEventEnd] = useState(new Date())
  return (
    <div className='login-form'>
      <form>
        <InputGroup
          value={title}
          onChange={e => setTitle(e.target.value)}
          placeholder='Title'
          className='login-form-item'
        />
        <DateTimePicker
          onChange={date => setEventStart(date)}
          value={eventStart}
        />
        <DateTimePicker
          onChange={date => setEventEnd(date)}
          value={eventEnd}
        />
        <Button text='Create Event' fill onClick={e => {
          e.preventDefault()
          props.createEvent(title, eventStart, eventEnd)
          props.close()
        }} type='submit'/>
      </form>
    </div>
  )
}
export default connect(null, {
  createEvent: Actions.events.createEvent,
})(CreateEvent)
