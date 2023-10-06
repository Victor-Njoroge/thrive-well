import React, { useState } from 'react'
import { Link } from 'react-router-dom'
function Navbar() {
    const [visible, setIsVisible]= useState(false)
    const [form, setIsForm]=useState(false)
    const handlePress = () =>{
        setIsForm(!form)
    }
    const handleClick = () =>{
        setIsVisible(!visible)
    }
  return (
    <div className='header'>

        
        
        <div className="navigation">
            <Link to='/'>Home</Link>
            <Link to='/doctors'>Doctors</Link>
            <Link to='/patients'>Patients</Link>
            <Link to='/appointment'>Appointments</Link>
            <Link to='/treatment'>Treatment</Link>
            <Link>Diseases</Link>
            <Link>Progress</Link>
        </div>
    </div>
  )
}

export default Navbar