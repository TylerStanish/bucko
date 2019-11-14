import React from 'react'
import {
  Navbar, Alignment, Button
} from '@blueprintjs/core'
import {connect} from 'react-redux'
import {push} from 'connected-react-router'
import actions from '../redux/actions'

const MyNavbar = props => {
  let rightIcon = <Button
    onClick={() => props.push('/login')}
    className='bp3-minimal' 
    icon='log-in'
    text='Log in'
  />
  let dashboardButton;
  if (props.token) {
    rightIcon = <Button
      onClick={() => props.logout()}
      className='bp3-minimal'
      icon='log-out'
      text='Log out'
    />
    dashboardButton = <Button
      onClick={() => props.push('/dashboard')}
      className='bp3-minimal'
      icon='dashboard'
      text='Dashboard'
    />
  }
  return (
    <Navbar>
      <Navbar.Group align={Alignment.LEFT}>
        <Navbar.Heading>Bucko</Navbar.Heading>
        {dashboardButton}
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
}, {
  logout: actions.auth.logout,
  push
})(MyNavbar)
