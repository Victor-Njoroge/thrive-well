import React, { useState } from 'react';
import axios from 'axios';

function FormDoctor() {
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
      const response = await axios.post('http://127.0.0.1:5555/create_doctor', formData);

      if (response.status === 201) {
        setMessage('Doctor created successfully');
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
        setError('An error occurred while creating the doctor.');
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

  const inputStyle = {
    width: '100%',
    padding: '10px',
    margin: '5px 0',
    border: '1px solid #ccc',
    borderRadius: '3px',
  };

  return (
    <div style={formStyle}>
      <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>Create Doctor</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="fname">First Name:</label>
          <input
            type="text"
            id="fname"
            name="fname"
            value={formData.fname}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="lname">Last Name:</label>
          <input
            type="text"
            id="lname"
            name="lname"
            value={formData.lname}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="phone_number">Phone Number:</label>
          <input
            type="tel"
            id="phone_number"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="regNo">Registration Number:</label>
          <input
            type="text"
            id="regNo"
            name="regNo"
            value={formData.regNo}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="gender">Gender:</label>
          <select
            id="gender"
            name="gender"
            value={formData.gender}
            onChange={handleChange}
            required
            style={inputStyle}
          >
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </div>
        <button type="submit" style={{ width: '100%', backgroundColor: '#007bff', color: '#fff', padding: '10px', border: 'none', borderRadius: '3px' }}>Create Doctor</button>
      </form>
      {message && <p>{message}</p>}
      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default FormDoctor;
