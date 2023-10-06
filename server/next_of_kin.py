from patients import db

class Next_of_kin(db.Model):
    __tablename__ = 'next_of_kin'


    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String, nullable=False)
    lname=db.Column(db.String, nullable=False)
    phone_number=db.Column(db.String, nullable=False)
    patient_id = db.Column(db.Integer,db.ForeignKey('patient.id'))

    
