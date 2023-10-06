from patients import db

class Doctor(db.Model):
    __tablename__ = 'doctor'

    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String, nullable=False)
    lname=db.Column(db.String, nullable=False)
    regNo = db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    phoneNo=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)
    gender=db.Column(db.String, nullable=False)
    hospital_id=db.Column(db.Integer, db.ForeignKey('hospital.id'))

    treatment=db.relationship('Treatment', backref='doctor')
    appointment=db.relationship('Appointment', backref='appointment')


    