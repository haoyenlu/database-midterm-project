
import { useState } from 'react';
import React from 'react'
import { Component } from 'react';
import MenuSet from './Container/MenuSet';
import Schedule from './Container/Schedule';
import Navbar from './Component/Navbar';
//import Products from '/product';
import { BrowserRouter as Router, Routes, Route, Link, Redirect} from 'react-router-dom';
import Home from './Home';
import Knownwater from './Knownwater';

function App(){
    return(
        <div className="App">
            <Routes>
                <Route path="/" element={<Home/>} />
                <Route path="/knownwater" element={<Knownwater/>} />
            </Routes>
        </div>
    );
}

export default App