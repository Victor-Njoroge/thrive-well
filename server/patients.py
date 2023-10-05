from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patient'

    id=db.Column(db.Integer, primary_key = True)
    fname=db.Column(db.String, nullable=False)
    lname=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    phone_number=db.Column(db.String, nullable=False)
    regNo=db.Column(db.String, nullable=False)
    gender=db.Column(db.String, nullable=False)

    treatment=db.relationship('Treatment',backref='patient')
    next_of_Kin=db.relationship('Next_of_kin', backref='patient')
    appointment=db.relationship('Appointment', backref='patient')

    