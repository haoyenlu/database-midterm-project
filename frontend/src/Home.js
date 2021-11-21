
import { useState } from 'react';
import MenuSet from './Container/MenuSet';
import Schedule from './Container/Schedule';
import Navbar from './Component/Navbar';
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from 'react-router-dom';


const Home = () => {

    const [city, setCity] = useState('宜蘭縣')
    const [town, setTown] = useState('頭城鎮')
    let now = new Date()
    const [date, setDate] = useState(now.getFullYear()+'/'+(now.getMonth()+1)+'/'+now.getDate())
    const [time, setTime] = useState('13:30')
    const [check, setCheck] = useState(false)

    return <>
        
        
        <Navbar />
        <MenuSet setCity={setCity} setTown={setTown} setTime={setTime} setDate={setDate} setCheck={setCheck}/>
        {check?<Schedule from={city} to={town} date={date} time={time}/>:<></>}
        
        
    </>

}

export default Home