import React from 'react'
import {
  Navbar, Alignment, Button
} from '@blueprintjs/core'
import {useHistory} from 'react-router-dom'
import {connect} from 'react-redux'
import actions from '../redux/actions'

const MyNavbar = props => {
  const history = useHistory()
  let rightIcon = <Button onClick={() => history.push('/login')} className='bp3-minimal' icon='log-in' text='Log in'/>
  if (props.token) {
    rightIcon = <Button onClick={() => props.logout()} className='bp3-minimal' icon='log-out' text='Log out'/>
  }
  return (
    <Navbar>
      <Navbar.Group align={Alignment.LEFT}>
        <Navbar.Heading>Bucko</Navbar.Heading>
      </Navbar.Group>
      <Navbar.Group align={Alignment.RIGHT}>
        {rightIcon}
      </Navbar.Group>
    </Navbar>
  )
}

export default connect(props => {
  return {
    token: props.auth.token
  }
}, {logout: actions.auth.logout})(MyNavbar)