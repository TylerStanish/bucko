import React from 'react'
import {
  Navbar, Alignment, Button
} from '@blueprintjs/core'
import {useHistory} from 'react-router-dom'

export default () => {
  const history = useHistory()
  return (
    <Navbar>
      <Navbar.Group align={Alignment.LEFT}>
        <Navbar.Heading>Bucko</Navbar.Heading>
      </Navbar.Group>
      <Navbar.Group align={Alignment.RIGHT}>
        <Button onClick={() => history.push('/login')} className='bp3-minimal' icon='log-in' text='Log in'/>
      </Navbar.Group>
    </Navbar>
  )
}