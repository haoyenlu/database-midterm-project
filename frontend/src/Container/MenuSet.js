import Stations from '../Component/Stations'
import Date from '../Component/Date'
import Time from '../Component/Time'
import '../App.css'
import { Space, Button } from 'antd'
import { RetweetOutlined } from '@ant-design/icons';

const MenuSet = ( { setFrom, setTo, setTime, setDate, setCheck } ) => {
    return (
        <div className='header'>
            <h1>全台遊憩水域天氣資訊系統</h1>
            <Space className='menu-set'>
                <div>
                    <div>縣市</div>
                    <Stations setFrom={setFrom} setCheck={setCheck}/>
                </div>
                {/* <RetweetOutlined style={{ fontSize: '25px'}}/> */}
                <div>
                    <div>鄉鎮市區</div>
                    <Stations setTo={setTo} setCheck={setCheck}/>
                </div>
                <div>
                    <div >日期</div>
                    <Date setDate={setDate} setCheck={setCheck}/>
                </div>
                <div>
                    <div>時間</div>
                    <Time setTime={setTime} setCheck={setCheck}/>
                </div>
                <Button onClick={()=>setCheck(true)}>查詢</Button>
            </Space>
        </div>
    )

}

export default MenuSet
