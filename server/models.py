from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()
db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(50))  
    lname = Column(String(50))  
    password = Column(String(8))  
    email = Column(String(100))  
    phone_number = Column(Integer)
    next_of_kin = relationship("NextOfKin", back_populates="patient")

class NextOfKin(db.Model):
    __tablename__ = 'next_of_kin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(50))  
    lname = Column(String(50))  
    phone_number = Column(Integer)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("Patient", back_populates="next_of_kin")
