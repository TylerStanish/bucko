import React from 'react'
import './App.css'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'

import '@blueprintjs/core/lib/css/blueprint.css'

import LandingPage from './pages/LandingPage'
import LoginPage from './pages/LoginPage'
import Navbar from './components/Navbar'

function App() {
  return (
    <Router>
      <Navbar/>
      <Switch>
        <Route path='/login'>
          <LoginPage/>
        </Route>
        <Route path='/'>
          <LandingPage/>
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
