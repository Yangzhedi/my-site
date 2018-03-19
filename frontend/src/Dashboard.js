import React from 'react';
import {Link, Route, Redirect} from 'react-router-dom';
import { connect } from 'react-redux'
import App from './App';
import { logout } from './Auth.redux'


function Er(){
    return <h2>Er</h2>
}
function San(){
    return <h2>San</h2>
}

@connect(
    state => state.auth,
    { logout }
)
class Dashboard extends React.Component {
    render(){
        const match = this.props.match;
        const redirectToLogin = <Redirect to='/login' />;
        const app = ( <div>
            <h1>123</h1>
            { this.props.isAuth? <button  onClick={this.props.logout}>注销</button>:null}
            <ul>
                <li>
                    <Link to={`${match.url}/`}>1</Link>
                </li>
                <li>
                    <Link to={`${match.url}/er`}>2</Link>
                </li>
                <li>
                    <Link to={`${match.url}/san`}>3</Link>
                </li>
            </ul>
            <Route path={`${match.url}/`} exact component={App} />
            <Route path={`${match.url}/er`} component={Er} />
            <Route path={`${match.url}/san`} component={San} />
        </div>);
        return this.props.isAuth ? app: redirectToLogin;
    }
}
export default Dashboard;