import React, { useState } from 'react';
import './PatientForm.css';

function PatientForm({ addPatient }) {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [gender, setGender] = useState('');
  const [age, setAge] = useState('');
  const [registrationNumber, setRegistrationNumber] = useState('');

  // const handleSubmit = (e) => {
  //   e.preventDefault();

  //   const patient = {
  //     firstName,
  //     lastName,
  //     gender,
  //     age,
  //     registrationNumber,
  //   };
    
  //   addPatient(patient);
    
  //   setFirstName('');
  //   setLastName('');
  //   setGender('');
  //   setAge('');
  //   setRegistrationNumber('');
  // };

  return (
    <div className='patient-form'>

      <div className='title'><h2>Patient's Form</h2></div>
   
      <form action="">
          <div className="input_field">
              <input
              type="text"
              placeholder="First Name"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              required
              /> 
          </div>
          <div className="input_field">
              <input
                type="text"
                placeholder="Last Name"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                required
              />
          </div>
          <div className="input_field">
              <input
                type="text"
                placeholder="Gender"
                value={gender}
                onChange={(e) => setGender(e.target.value)}
                required
              />
          </div>
          <div className="input_field">
              <input
                type="number"
                placeholder="Age"
                value={age}
                onChange={(e) => setAge(e.target.value)}
                required
              />
          </div>
          <div className="input_field">
              <input
                type="text"
                placeholder="Registration Number"
                value={registrationNumber}
                onChange={(e) => setRegistrationNumber(e.target.value)}
                required
              />
          </div>
          <div className="input_field">
              <input type="submit" value="Submit"/> 
          </div>
      </form> 
    </div>
  );
}

export default PatientForm;
