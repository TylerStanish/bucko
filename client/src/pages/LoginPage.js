import React, {useState} from 'react'
import { FormGroup, InputGroup, Button } from '@blueprintjs/core'

export default () => {
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
        />
        <Button text='Log in' fill onClick={e => {e.preventDefault(); console.log('hi');}} type='submit'/>
      </form>
    </div>
  )
}