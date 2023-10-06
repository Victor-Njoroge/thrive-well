import React, { useState } from 'react';
import axios from 'axios'; // Import Axios

function FormTreatment() {
  const [formData, setFormData] = useState({
    patient_regNo: '',
    doctor_regNo: '',
    progress: '',
  });

  const [message, setMessage] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.patch('http://127.0.0.1:5555/update_treatment_progress', formData);

      if (response.status === 200) {
        setMessage('Treatment progress updated successfully');
      } else if (response.status === 404) {
        setMessage(response.data.message);
      } else {
        setMessage('An error occurred while updating treatment progress');
      }
    } catch (error) {
      setMessage('An error occurred while updating treatment progress');
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '0 auto' }}>
      <h2 style={{ textAlign: 'center' }}>Update Treatment Progress</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="patient_regNo">Patient Registration Number:</label>
          <input
            type="text"
            id="patient_regNo"
            name="patient_regNo"
            value={formData.patient_regNo}
            onChange={handleInputChange}
            required
            style={{ width: '100%', padding: '5px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="doctor_regNo">Doctor Registration Number:</label>
          <input
            type="text"
            id="doctor_regNo"
            name="doctor_regNo"
            value={formData.doctor_regNo}
            onChange={handleInputChange}
            required
            style={{ width: '100%', padding: '5px' }}
          />
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label htmlFor="progress">New Progress:</label>
          <input
            type="text"
            id="progress"
            name="progress"
            value={formData.progress}
            onChange={handleInputChange}
            required
            style={{ width: '100%', padding: '5px' }}
          />
        </div>
        <div>
          <button
            type="submit"
            style={{
              backgroundColor: '#007bff',
              color: 'white',
              border: 'none',
              padding: '10px 15px',
              cursor: 'pointer',
            }}
          >
            Update Progress
          </button>
        </div>
      </form>
      {message && (
        <p
          style={{
            marginTop: '10px',
            color: message.includes('successfully') ? 'green' : 'red',
          }}
        >
          {message}
        </p>
      )}
    </div>
  );
}

export default FormTreatment;
