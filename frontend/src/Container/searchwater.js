import Stations from '../Component/Stations'
import Date from '../Component/Date'
import Time from '../Component/Time'
import '../App.css'
import { Space, Button } from 'antd'
import { RetweetOutlined } from '@ant-design/icons';

const SearchWater = ( { setFrom, setTo, setTime, setDate, setCheck } ) => {
    return (
        <div className='header'>
            <h1>搜尋已知水域資料</h1>
                <div class="wrap">
                    <div class="search">
                        <input type="text" class="searchTerm" placeholder="     想查詢已知的水域?"/>
                        {/* <button type="submit" class="searchButton">
                            <i class="fa fa-search"></i>
                        </button> */}
                        
                    </div>
                </div>
                <br></br>
            <Button onClick={()=>setCheck(true)}>查詢</Button>
        </div> 
        
    )
    

}

export default SearchWater
