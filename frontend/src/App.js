import React, { Component } from 'react';
import { connect } from 'react-redux';
import { addCountAsync,subCount, addCount } from "./index.redux";
import logo from './logo.svg';
import './App.css';
import {Button} from 'antd-mobile'

// const mapStatetoProps = state => {
//     return {num:state}
// };
// const actionCreator = { addCountAsync,subCount, addCount };
// 装饰器的写法
// App = connect(mapStatetoProps, actionCreator)(App);


@connect(
    // 你要state的什么属性，放在props里
    state => ({num:state.counter}),
    // 你要什么方法，放在props里，自动dispatch
    { addCountAsync,subCount, addCount }
)
class App extends Component {
    render() {
        const num = this.props.num;
        const addCount = this.props.addCount;
        const subCount = this.props.subCount;
        const addCountAsync = this.props.addCountAsync;
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h1 className="App-title">现在有数字{num}</h1>
                </header>
                <Button type='primary' onClick={addCount}> 加 </Button>
                <Button type='primary' onClick={subCount}> - </Button>
                <Button type='primary' onClick={addCountAsync}> 拖两天 </Button>
            </div>
        );
    }
}

export default App;
