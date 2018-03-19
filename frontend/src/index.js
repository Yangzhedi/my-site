import React from 'react';
import ReactDOM from 'react-dom';
import { createStore, applyMiddleware, compose } from 'redux'
import thunk from 'redux-thunk'
import { Provider } from 'react-redux'
import { BrowserRouter, Route, Redirect, Switch } from 'react-router-dom'

// import './index.css';
// import { counter } from "./index.redux";
import reducers from './reducer'
import Auth from './Auth'
import Dashboard from './Dashboard'
import './config'
// import registerServiceWorker from './registerServiceWorker';
// registerServiceWorker();

const reduxDevtools = window.devToolsExtension ? window.devToolsExtension() : f => f;

// applyMiddleware 管理中间件
const store = createStore(reducers, compose(
    applyMiddleware(thunk),
    reduxDevtools
));
// class Test extends React.Component{
//     render(){
//         console.log(this.props);
//         return <h2>测试  {this.props.match.params.location}</h2>
//     }
// }


ReactDOM.render(
    <Provider store={store}>
        <BrowserRouter>
            {/*<App />*/}
            <Switch>
                {/*只渲染命中的第一个Route*/}
                <Route path='/login' exact component={Auth} />
                <Route path='/dashboard' component={Dashboard} />
                <Redirect to='/dashboard' />
            </Switch>
        </BrowserRouter>
    </Provider>,
    document.getElementById('root')
);
