import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

const Appointments = () => {
  const [selectedDate, setSelectedDate] = useState(null);
  const [appointments, setAppointments] = useState([]);
  const [day, setDay] = useState('');
  const [time, setTime] = useState('');
  const [patient, setPatient] = useState('');

  const handleDateSelect = (date) => {
    setSelectedDate(date);
    // You can fetch appointments for the selected date from your backend here.
    // For simplicity, we'll simulate the data.
    const mockAppointments = [
      { id: 1, day: '2023-10-05', time: '10:00 AM', patient: '1234' },
      { id: 2, day: '2023-10-05', time: '11:00 AM', patient: '5678' },
    ];
    setAppointments(mockAppointments);
  };

  const handleAddAppointment = () => {
    if (day && time && patient) {
      // You can send the new appointment data to your backend here for storage.
      // For simplicity, we'll just update the state with the new appointment.
      setAppointments([...appointments, { id: appointments.length + 1, day, time, patient }]);
      setDay('');
      setTime('');
      setPatient('');
    }
  };

  return (
    <div>
      <h1>Appointment Management System</h1>
      <div>
        <h2>Calendar</h2>
        <DatePicker selected={selectedDate} onChange={handleDateSelect} />
      </div>
      {selectedDate && (
        <div>
          <h2>Appointments for {selectedDate.toDateString()}</h2>
          <ul>
            {appointments.map((appointment) => (
              <li key={appointment.id}>
                {appointment.time} | Patient: {appointment.patient}
              </li>
            ))}
          </ul>
        </div>
      )}
      <div>
        <h2>Add Appointment</h2>
        <input
          type="text"
          placeholder="Day"
          value={day}
          onChange={(e) => setDay(e.target.value)}
        />
        <input
          type="text"
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
      </div>
    </div>
  );
};

export default Appointments;
