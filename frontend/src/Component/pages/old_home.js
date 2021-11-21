// this is copied from the original App.js

import { useState } from 'react';
import MenuSet from '../../Container/MenuSet.js';
import Schedule from '../../Container/Schedule.js';
import Navbar from '../Navbar';
//import Products from '/product';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


const App = () => {

    const [from, setFrom] = useState('宜蘭縣')
    const [to, setTo] = useState('頭城鎮')
    let now = new Date()
    const [date, setDate] = useState(now.getFullYear()+'/'+(now.getMonth()+1)+'/'+now.getDate())
    const [time, setTime] = useState('13:30')
    const [check, setCheck] = useState(false)

    return <>
        
        
        <Router>
        <Navbar />
        <MenuSet setFrom={setFrom} setTo={setTo} setTime={setTime} setDate={setDate} setCheck={setCheck}/>
        {check?<Schedule from={from} to={to} date={date} time={time}/>:<></>}
        <Routes>
            {/* <Route path='/products' component={Products} /> */}
            <MenuSet setFrom={setFrom} setTo={setTo} setTime={setTime} setDate={setDate} setCheck={setCheck}/>
            {check?<Schedule from={from} to={to} date={date} time={time}/>:<></>}
        </Routes>
      </Router>
    </>

}

export default App


