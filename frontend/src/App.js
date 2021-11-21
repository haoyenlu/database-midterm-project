
import { useState } from 'react';
import React from 'react'
import { Component } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, Redirect} from 'react-router-dom';
import Home from './Home';
import Knownwater from './Knownwater';
import Other from './other';

function App(){
    return(
        <div className="App">
            <Routes>
                <Route path="/" element={<Home/>} />
                <Route path="/knownwater" element={<Knownwater/>} />
                <Route path="/other" element={<Other/>} />
            </Routes>
        </div>
    );
}

export default App