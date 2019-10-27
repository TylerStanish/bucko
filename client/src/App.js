import React from 'react'
import './App.css'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'
import { ConnectedRouter, routerMiddleware } from 'connected-react-router'
import {createStore, applyMiddleware, compose} from "redux";
import {Provider} from 'react-redux'
import {createBrowserHistory} from 'history'
import reduxThunk from 'redux-thunk'

import '@blueprintjs/core/lib/css/blueprint.css'

import LandingPage from './pages/LandingPage'
import LoginPage from './pages/LoginPage'
import Navbar from './components/Navbar'
import reducers from './redux/reducers'

const history = createBrowserHistory()
const store = createStore(reducers(history), compose(applyMiddleware(routerMiddleware(history), reduxThunk)))

function App() {
  return (
    <Provider store={store}>
      <ConnectedRouter history={history}>
        {/* <Router> */}
          <Navbar/>
          <Switch>
            <Route path='/login'>
              <LoginPage/>
            </Route>
            <Route path='/'>
              <LandingPage/>
            </Route>
          </Switch>
        {/* </Router> */}
      </ConnectedRouter>
    </Provider>
  );
}

export default App;
