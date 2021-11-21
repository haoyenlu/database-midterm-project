import { Select } from 'antd';
import 'antd/dist/antd.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

const { Option } = Select;

const Stations = ({ setFrom, setTo, setCheck }) => {

    const [stations, setStations] = useState([])

    useEffect(() => {
        axios.get('http://127.0.0.1:3000/api/town_lists')
        .then((res) => { 
          setStations(res.data)
        })
        .catch((error) => { console.log(error) })
    },[])

    const onChange = (value) => {
        console.log(`selected ${value}`);
        setFrom ? setFrom(value) : setTo(value)
        setCheck(false)
      }
      
    const onSearch = (val) => {
        console.log('search:', val);
      }
      
      return(
        <Select
          showSearch
          style={{ width: 200 }}
          defaultValue={setFrom?"宜蘭縣":"頭城鎮"}
          onChange={onChange}
          onSearch={onSearch}
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
        {stations.map((station)=>{
            return <Option value={station['station_name']}>{station['station_name']}</Option>
        })}
        </Select>
      );

}



export default Stations