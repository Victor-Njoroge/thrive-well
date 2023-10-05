import React, { useState } from 'react';
import PatientForm from "./Components/PatientForm";
import PatientList from "./Components/PatientList"

function App() {


  return (
    <div className="App">
      <PatientForm />
      <PatientList />
    </div>
  );
}

export default App;
