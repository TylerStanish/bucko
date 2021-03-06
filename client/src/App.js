import React from 'react'
import './App.css'
import {
  Switch,
  Route
} from 'react-router-dom'
import { ConnectedRouter, routerMiddleware } from 'connected-react-router'
import {createStore, applyMiddleware, compose} from "redux";
import {Provider, connect} from 'react-redux'
import {createBrowserHistory} from 'history'
import reduxThunk from 'redux-thunk'

import '@blueprintjs/core/lib/css/blueprint.css'
import '@blueprintjs/datetime/lib/css/blueprint-datetime.css'

import LandingPage from './pages/LandingPage'
import LoginPage from './pages/LoginPage'
import Navbar from './components/Navbar'
import reducers from './redux/reducers'

import Actions from './redux/actions'
import DashboardPage from './pages/DashboardPage';

const history = createBrowserHistory()
const store = createStore(reducers(history), compose(applyMiddleware(routerMiddleware(history), reduxThunk)))

function Main(props) {
  props.getTokenFromLocalStorage()
  return (
    <>
      <Navbar/>
      <Switch>
        <Route path='/login'>
          <LoginPage/>
        </Route>
        <Route path='/dashboard'>
          <DashboardPage/>
        </Route>
        <Route path='/'>
          <LandingPage/>
        </Route>
      </Switch>
    </>
  )
}

Main = connect(null, {getTokenFromLocalStorage: Actions.auth.getTokenFromLocalStorage})(Main)

function App() {
  return (
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <Main/>
      </ConnectedRouter>
    </Provider>
  );
}

export default App
