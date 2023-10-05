from patients import db


class Appointment(db.Model):

    __tablename__ = "appointment"


    id = db.Column(db.Integer, primary_key=True)
    doctor_id=db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id=db.Column(db.Integer, db.ForeignKey('patient.id'))
    appointment_date=db.Column(db.Date, nullable=False)
    appointment_time=db.Column(db.Time, nullable=False)

    