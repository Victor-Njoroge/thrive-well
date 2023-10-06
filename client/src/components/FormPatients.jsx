import React, { useState } from 'react';
import axios from 'axios';

function FormPatient() {
  const [formData, setFormData] = useState({
    fname: '',
    lname: '',
    password: '',
    email: '',
    phone_number: '',
    regNo: '',
    gender: '',
  });

  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:5555/create_patient', formData);

      if (response.status === 201) {
        setMessage('Patient created successfully');
        // Clear the form
        setFormData({
          fname: '',
          lname: '',
          password: '',
          email: '',
          phone_number: '',
          regNo: '',
          gender: '',
        });
      }
    } catch (err) {
      if (err.response) {
        setError(err.response.data.error);
      } else {
        setError('An error occurred while creating the patient.');
      }
    }
  };

  const formStyle = {
    maxWidth: '400px',
    margin: '0 auto',
    padding: '20px',
    backgroundColor: '#f5f5f5',
    border: '1px solid #ccc',
    borderRadius: '5px',
  };

  const labelStyle = {
    marginBottom: '5px',
    fontWeight: 'bold',
  };

  const inputStyle = {
    marginBottom: '10px',
    padding: '8px',
    border: '1px solid #ccc',
    borderRadius: '4px',
    fontSize: '16px',
    width: '20rem',
  };

  const buttonStyle = {
    backgroundColor: '#007bff',
    color: '#fff',
    border: 'none',
    borderRadius: '4px',
    padding: '10px 15px',
    fontSize: '16px',
    cursor: 'pointer',
  };

  const messageStyle = {
    marginTop: '10px',
    color: '#007bff',
    fontWeight: 'bold',
  };

  const errorStyle = {
    marginTop: '10px',
    color: '#ff0000',
    fontWeight: 'bold',
  };

  return (
    <div style={formStyle}>
      <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>Create Patient</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label style={labelStyle}>First Name:</label>
          <input
            type="text"
            name="fname"
            value={formData.fname}
            onChange={handleChange}
            style={inputStyle}
          />
        </div>
        <div>
          <label style={labelStyle}>Last Name:</label>
          <input
            type="text"
            name="lname"
            value={formData.lname}
            onChange={handleChange}
            style={inputStyle}
          />
        </div>
        <div>
          <label style={labelStyle}>Password:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            style={inputStyle}
          />
        </div>
        <div>
          <label style={labelStyle}>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            style={inputStyle}
          />
        </div>
        <div>
          <label style={labelStyle}>Phone Number:</label>
          <input
            type="text"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleChange}
            style={inputStyle}
          />
        </div>
        <div>
          <label style={labelStyle}>Registration Number:</label>
          <input
            type="text"
            name="regNo"
            value={formData.regNo}
            onChange={handleChange}
            style={inputStyle}
          />
        </div>
        <div>
          <label style={labelStyle}>Gender:</label>
          <input
            type="text"
            name="gender"
            value={formData.gender}
            onChange={handleChange}
            style={inputStyle}
          />
        </div>
        <button type="submit" style={buttonStyle}>Create Patient</button>
      </form>
      {message && <p style={messageStyle}>{message}</p>}
      {error && <p style={errorStyle}>Error: {error}</p>}
    </div>
  );
}

export default FormPatient;
