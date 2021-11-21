
import { useState } from 'react';
import MenuSet from './Container/MenuSet';
import Schedule from './Container/Schedule';
import Navbar from './Component/Navbar';
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from 'react-router-dom';


const Home = () => {

    const [from, setFrom] = useState('宜蘭縣')
    const [to, setTo] = useState('頭城鎮')
    let now = new Date()
    const [date, setDate] = useState(now.getFullYear()+'/'+(now.getMonth()+1)+'/'+now.getDate())
    const [time, setTime] = useState('13:30')
    const [check, setCheck] = useState(false)

    return <>
        
        
        <Navbar />
        <MenuSet setFrom={setFrom} setTo={setTo} setTime={setTime} setDate={setDate} setCheck={setCheck}/>
        {check?<Schedule from={from} to={to} date={date} time={time}/>:<></>}
        
        
    </>

}

export default Home