from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Patient, NextOfKin


engine = create_engine('sqlite:///hospital_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# Initialize the database
Base.metadata.create_all(engine)

# Seed initial data
data = [
    {
        'patient': {'fname': 'Kim', 'lname': 'Him', 'password': '12345678', 'email': 'kim.him@gmail.com', 'phone_number': 254708978665},
        'next_of_kin': {'fname': 'Jane', 'lname': 'Grace', 'phone_number': 123456789}
    },
    {
        'patient': {'fname': 'Chris', 'lname': 'Martin', 'password': '98765432', 'email': 'ahmed@gmail.com', 'phone_number': 254722949866},
        'next_of_kin': {'fname': 'Margin', 'lname': 'Three', 'phone_number': 987654321}
    },
    {
        'patient': {'fname': 'Ahmed', 'lname': 'Taylor', 'password': '76857483', 'email': 'taylor@gmail.com', 'phone_number': 254769060861},
        'next_of_kin': {'fname': 'Wood', 'lname': 'Greenwood', 'phone_number': 87654321}
    },
    {
        'patient': {'fname': 'John', 'lname': 'Chris', 'password': '67546548', 'email': 'oxford@gmail.com', 'phone_number': 254765836738},
        'next_of_kin': {'fname': 'Lame', 'lname': 'Lane', 'phone_number': 456789123}
    }
]

session = DBSession()

for item in data:
    # Create the patient
    patient = Patient(**item['patient'])
    session.add(patient)
    
    # Create the next of kin and associate it with the patient
    next_of_kin = NextOfKin(**item['next_of_kin'], patient=patient)
    session.add(next_of_kin)

session.commit()
session.close()
