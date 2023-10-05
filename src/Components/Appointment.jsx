import React, { useState, useEffect } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import './Appointment.css'

const Appointments = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [appointments, setAppointments] = useState([]);
  const [day, setDay] = useState('');
  const [time, setTime] = useState('');
  const [patient, setPatient] = useState('');

  useEffect(() => {
    // Fetch and set appointments for the current date.
    // replace this with backend data (fetching).
    const mockAppointments = [
      { id: 1, day: '2023-10-05', time: '10:00 AM', patient: '1234' },
      { id: 2, day: '2023-10-05', time: '11:00 AM', patient: '5678' },
    ];
    setAppointments(mockAppointments);
  }, []);

  const handleDateSelect = (date) => {
    setSelectedDate(date);
    console.log(date.toDateString())
    var date = date.toDateString();
    date = date.split(" ")
    // fetch appointments for the selected date from backend.
    // sample data.
    // fetch(`http://localhost?year=${date[3]}&month=${date[2]}&day=${date[1]}`)
    const mockAppointments = [
      { id: 1, day: '2023-10-05', time: '10:00 AM', patient: '1234' },
      { id: 2, day: '2023-10-05', time: '11:00 AM', patient: '5678' },
    ];
    setAppointments(mockAppointments);
  };

  const handleAddAppointment = () => {
    if (day && time && patient) {
      // Can send the new appointment data to the backend here for storage.
      // For simplicity, we'll just update the state with the new appointment.
      setAppointments([...appointments, { id: appointments.length + 1, day, time, patient }]);
      setDay('');
      setTime('');
      setPatient('');
    }
  };

  return (
    <div className='Appointment'>
        <div className="title">
        <h1>Appointments</h1>
        </div>
        <div className="calender_frame">
            <h1>Calender</h1>
            <Calendar value={selectedDate} onChange={handleDateSelect} />
        </div>
        <div className="patient_list">
        <h2>Appointments for {selectedDate.toDateString()}</h2>
        <div className="time_appointments">
          <div className="time_lines"><p>7:00 AM</p></div>
          <div className="time_lines"><p>8:00 AM</p></div>
          <div className="time_lines"><p>9:00 AM</p> </div>
          <div className="time_lines"><p>10:00 AM</p></div>
          <div className="time_lines"><p>11:00 AM</p></div>
          <div className="time_lines"><p>12:00 PM</p></div>
          <div className="time_lines"><p>1:00 AM</p></div>
          <div className="time_lines"><p>2:00 AM</p></div>
          <div className="time_lines"><p>3:00 AM</p></div>
          <div className="time_lines"><p>4:00 AM</p></div>
          <div className="time_lines"><p>5:00 AM</p></div>
          <div className="time_lines"><p>6:00 AM</p></div>
          {appointments.map((appointment) => (
            <div className="time_lines" key={appointment.id}>
              Patient: {appointment.patient}
            </div>
          ))}
        </div>
      </div>
      <form action="#">
        <h2>Add Appointment</h2>
        <input
          type="date"
          placeholder="Date"
          value={day}
          onChange={(e) => setDay(e.target.value)}
        />
        <input
          type="time"
          placeholder="Time"
          value={time}
          onChange={(e) => setTime(e.target.value)}
        />
        
        <input
          type="text"
          placeholder="Patient's Registration Number"
          value={patient}
          onChange={(e) => setPatient(e.target.value)}
        />
        

        <button onClick={handleAddAppointment}>Add Appointment</button>
      </form>
    </div>
  );
};

export default Appointments;
