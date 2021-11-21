import Table from '../Component/Table'
import ScheduleHeader from '../Component/ScheduleHeader';
import Fare from '../Component/Fare';


const AllWater = ({ from, to, date, time }) => {

    return(
        <div className='allwater'>
            <ScheduleHeader from={from} to={to} date={date} time={time} />
            <Table from={from} to={to} date={date} time={time}/>
            {/* <Fare from={from} to={to} date={date}/> */}
        </div>
    )
}

export default AllWater