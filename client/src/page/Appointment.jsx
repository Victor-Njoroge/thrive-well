import React, { useState, useEffect } from 'react';
import axios from 'axios';
import FormUpdate from '../components/FormUpdate';

function AppointmentList() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5555/appointments')
      .then((response) => {
        setAppointments(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Appointment List</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Doctor Registration No</th>
            <th>Patient Registration No</th>
            <th>Appointment Date</th>
            <th>Appointment Time</th>
          </tr>
        </thead>
        <tbody>
          {appointments.map((appointment) => (
            <tr key={appointment.id}>
              <td>{appointment.id}</td>
              <td>{appointment.doctor_regNo}</td>
              <td>{appointment.patient_regNo}</td>
              <td>{appointment.appointment_date}</td>
              <td>{appointment.appointment_time}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <FormUpdate/>
    </div>
  );
}

export default AppointmentList;
