from patients import db

class Treatment(db.Model):
    __tablename__ = 'treatment'

    id=db.Column(db.Integer, primary_key=True)
    patient_id=db.Column(db.Integer, db.ForeignKey('patient.id'))
    disease_id=db.Column(db.Integer, db.ForeignKey('disease.id'))
    hospital_id=db.Column(db.Integer,db.ForeignKey('hospital.id'))
    doctor_id=db.Column(db.Integer, db.ForeignKey('doctor.id'))

    progress=db.relationship('Progress', backref='treatment')



    