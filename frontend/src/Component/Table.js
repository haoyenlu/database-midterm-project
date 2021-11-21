import { Table } from 'antd';
import { CheckOutlined, CloseOutlined } from '@ant-design/icons';
import axios from 'axios';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';





const Tab = ({ from, to, date, time }) => {
  const [click, setClick] = useState(false);
  const closeMobileMenu = () => setClick(false);
  const [tabel, setTable] = useState([])

  useEffect(() => {
    axios.post('http://127.0.0.1:8000/api/timetable/search', {
      "StartStation": from,
      "EndStation": to,
      "OutWardSearchDate": date,
      "OutWardSearchTime": time
    })
    .then((res) => { 
      setTable(res.data)
    })
    .catch((error) => { console.log(error) })
  },[])

  const columns = [
    {
      title: '水域名稱',  //原本是出發時間
      dataIndex: 'waterName', //原本是startTime
      key: 'waterName',  //原本是name
    },
    {
      title: '水域類別',  //原本是行車時間
      dataIndex: 'category', //原本是timeSpend
      key: 'category', //原本是timeSpend
    },
    {
      title: '氣溫',  //原本是抵達時間
      dataIndex: 'temperature', //原本是arrivalTime
      key: 'temperature', //原本是arrivalTime
    },
    {
      title: '天氣狀況',  //原本是車次
      key: 'weatherCondition',  //原本是number
      dataIndex: 'weatherCondition',  //原本是number
    },
    {
      title: '是否為浪點',  //原本是是否適用早鳥
      key: 'surfSpotCheck', //原本是earlyBird
      dataIndex: 'surfSpotCheck', //原本是earlyBird
      render: surfSpotCheck => (
        <>
          {surfSpotCheck 
          ? <Link to='/surfspotdetails' className='nav-links' onClick={closeMobileMenu}>
              點擊取得該浪點詳細資訊
            </Link>
          :<CloseOutlined />}
        </>
      ),
    },

  ];
  
  
  return <Table columns={columns} dataSource={tabel} />
}

export default Tab