import React, {useState} from 'react'
import { InputGroup, Button } from '@blueprintjs/core'
import { connect } from 'react-redux'

import Actions from '../redux/actions'

const LoginPage = props => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  return (
    <div className='login-form'>
      <form>
        <InputGroup
          value={email}
          onChange={e => setEmail(e.target.value)}
          placeholder='Email'
          className='login-form-item'
        />
        <InputGroup
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder='Password'
          className='login-form-item'
          type='password'
        />
        <Button text='Log in' fill onClick={e => {
          e.preventDefault()
          if (!email || !password) {
            alert('Missing email and/or password')
            return
          }
          props.login(email, password)
        }} loading={props.loginLoading} type='submit'/>
        <Button text='Sign up' fill onClick={e => {
          e.preventDefault()
          if (!email || !password) {
            alert('Missing email and/or password')
            return
          }
          props.signup(email, password)
        }} loading={props.signupLoading} type='submit'/>
      </form>
    </div>
  )
}
export default connect(state => {
  return {
    loginLoading: state.auth.loginLoading,
    signupLoading: state.auth.signupLoading
  }
}, {
  login: Actions.auth.login,
  signup: Actions.auth.signup
})(LoginPage)
