import { Select } from 'antd';
import 'antd/dist/antd.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

const { Option } = Select;

const Stations = ({ options,setCities,setTowns, setCity,setTown, setCheck ,isCity}) => {


    useEffect(() => {
      if (isCity){
        axios.get('http://127.0.0.1:8000/api/town_list')
        .then((res) => { 
          var _tempCity = [];
          res.data.forEach(element => {
            _tempCity.push(element[0]);
          });
          setCities(_tempCity);

        })
        .catch((error) => { console.log(error) })
      }
    },[])

    const onChange = (value) => {
      if (isCity){
        axios.post('http://127.0.0.1:8000/api/town_list',{
          "city":value
        })
        .then((res) => { 
          var _tempTown = [];
          res.data.forEach(element => {
            _tempTown.push(element[0]);
          });
          setTowns(_tempTown);
        })
        .catch((error) => { console.log(error) })
        setCity(value);
        setCheck(false)
      }
      else{
        setTown(value)
      }
    }
      
    const onSearch = (val) => {
        console.log('search:', val);
    }
      
      return(
        <Select
          showSearch
          style={{ width: 200 }}
          defaultValue={options[0]}
          onChange={onChange}
          onSearch={onSearch}
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }
        >
        {options.map((option)=>{
          return <Option value={option}>{option}</Option>
        })}
        </Select>
      );

}



export default Stations