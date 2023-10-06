import React, { useState } from 'react';
import axios from 'axios';
import Swal from 'sweetalert2';  // Import SweetAlert

function FormUpdate() {
  const [id, setId] = useState('');
  const [appointmentDate, setAppointmentDate] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.patch(`http://127.0.0.1:5555/update_appointment/${id}`, {
        appointment_date: appointmentDate,
      });

      if (response.status === 200) {
        // Display a SweetAlert success notification
        Swal.fire({
          icon: 'success',
          title: 'Success',
          text: 'Appointment date updated successfully',
        }).then(() => {
          // Reload the page after closing the SweetAlert dialog
          window.location.reload();
        });
      }
    } catch (err) {
      if (err.response) {
        setError(err.response.data.error);
      } else {
        setError('An error occurred while updating the appointment date.');
      }
    }
  };

  return (
    <div>
      <h2>Update Appointment Date</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Appointment ID:</label>
          <input
            type="number"
            value={id}
            onChange={(e) => setId(e.target.value)}
          />
        </div>
        <div>
          <label>New Appointment Date:</label>
          <input
            type="date"
            value={appointmentDate}
            onChange={(e) => setAppointmentDate(e.target.value)}
          />
        </div>
        <button type="submit">Update Appointment Date</button>
      </form>
      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default FormUpdate;
