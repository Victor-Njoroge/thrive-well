import { useState } from 'react'
import { BrowserRouter, Routes, Route,} from 'react-router-dom';
import Navbar from './components/Navbar';
import './App.css'
import Home from './page/Home';
import Appointments from './page/Appointment';
import Progress from './page/Progress';
import Patient from './page/Patient';
import Doctor from './page/Doctor';
import Treatment from './page/Treatment';


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
        <Navbar/>
        <Routes>
            <Route exact path='/' element={<Home/>}/>
            <Route exact path='/appointment' element={<Appointments/>}/>
            <Route exact path='/patients' element={<Patient/>}/>
            <Route exact path='/doctors' element={<Doctor/>}/>
            <Route exact path='/treatment' element={<Treatment/>}/>
        </Routes>
      
      </BrowserRouter>
    </>
  )
}

export default App
