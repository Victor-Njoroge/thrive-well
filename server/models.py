from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    password = Column(String(8))
    email = Column(String)
    phone_number = Column(Integer)
    next_of_kin = relationship("NextOfKin", back_populates="patient")

class NextOfKin(Base):
    __tablename__ = 'next_of_kin'
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    phone_number = Column(Integer)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("Patient", back_populates="next_of_kin")
