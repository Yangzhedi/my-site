import React from 'react';
import { Redirect} from 'react-router-dom'
import { connect } from 'react-redux'
import { login, getUserData } from './Auth.redux'
import axios from "axios";

@connect(
    state => state.auth,
    {login, getUserData}
)
class Auth extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            data: {}
        }
    }

    componentDidMount(){
        // this.props.getUserData()
        axios.get('/hello')
            .then( res => {
                if (res.status === 200) {
                    // dispatch(userData(res.data));
                    console.log(res.data)
                }
            })
    }

    render(){
        return (
            <div>
                <h2>我的名字是{this.props.user},年龄是{this.props.age}</h2>
                { this.props.isAuth ? <Redirect to='/dashboard' /> : null}
                <h2> 你没有权限，需要登录 </h2>
                <button onClick={this.props.login}>登录</button>
            </div>
        )
    }

}
export default Auth;