
import { useState } from 'react';
import MenuSet from './Container/MenuSet';
import SearchWater from './Container/searchwater';
import Navbar from './Component/Navbar';
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from 'react-router-dom';
import AllWater from './Container/allwater';



const Knownwater = () => {

    const [from, setFrom] = useState('宜蘭縣')
    const [to, setTo] = useState('頭城鎮')
    let now = new Date()
    const [date, setDate] = useState(now.getFullYear()+'/'+(now.getMonth()+1)+'/'+now.getDate())
    const [time, setTime] = useState('13:30')
    const [check, setCheck] = useState(false)

    return <>
        
        
        <Navbar />
       
        <SearchWater setFrom={setFrom} setTo={setTo} setTime={setTime} setDate={setDate} setCheck={setCheck}/>
        {check?<AllWater from={from} to={to} date={date} time={time}/>:<></>}
        
        
        
    </>

}

export default Knownwater