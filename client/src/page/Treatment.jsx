import React, { useState, useEffect } from 'react';
import axios from 'axios';
import FormTreatment from '../components/FormTreatment';

function Treatment() {
  const [treatments, setTreatments] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:5555/get_treatments')
      .then((response) => {
        setTreatments(response.data.treatments);
      })
      .catch((err) => {
        setError('An error occurred while fetching treatments.');
      });
  }, []);

  return (
    <div>
      <h2>Treatments</h2>
      {error && <p>Error: {error}</p>}
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Patient RegNo</th>
            <th>Doctor RegNo</th>
            <th>Disease ID</th>
            <th>Hospital ID</th>
          </tr>
        </thead>
        <tbody>
          {treatments.map((treatment) => (
            <tr key={treatment.id}>
              <td>{treatment.id}</td>
              <td>{treatment.patient_regNo}</td>
              <td>{treatment.doctor_regNo}</td>
              <td>{treatment.disease_id}</td>
              <td>{treatment.hospital_id}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <FormTreatment/>
    </div>
  );
}

export default Treatment;
