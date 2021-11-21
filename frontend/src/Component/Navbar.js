import React, {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
import {Button} from './Button';


function Navbar() {
    const [click, setClick] = useState(false);
    const [button,setButton] = useState(true);

    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);

    const showButton = () => {
        if(window.innerWidth <= 960){
            setButton(false);
        }else{
            setButton(true);
        }
    };

    useEffect(() => {
        showButton();
    }, []);

    window.addEventListener('resize', showButton);

    return (
        <>
            <nav className="navbar">
                <div className=".navbar-container">
                    <Link to="/" className="navbar-logo" onClick={closeMobileMenu}>
                        水域氣象<i class="fas fa-cloud-showers-heavy"></i>
                    </Link>  
                    <div className='menu-icon' onClick={handleClick}>
                       <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                    </div>  
                    <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                        
                        <li className='nav-item'>
                            <Link to='/' className='nav-links' onClick={closeMobileMenu}>
                                用區域搜尋海域
                            </Link>
                        </li>
                        <li className='nav-item'>
                            <Link to='/knownwater' className='nav-links' onClick={closeMobileMenu}>
                                查看已知海域
                            </Link>
                        </li>
                        <li className='nav-item'>
                            <Link to='/other' className='nav-links' onClick={closeMobileMenu}>
                                其他/熱門海域
                            </Link>
                        </li>
                        {button && <Button buttonStyle='btn--outline'>SIGN UP</Button>}
                    </ul> 
                    
                </div>
            </nav>
        </>
    )
}

export default Navbar
