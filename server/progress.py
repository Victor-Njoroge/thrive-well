from patients import db

class Progress(db.Model):
    __tablename__ = 'progress'

    id=db.Column(db.Integer, primary_key=True)
    treatment_id=db.Column(db.Integer, db.ForeignKey('treatment.id'))
    medical_condition=db.Column(db.String, nullable=False)
    vital_signs=db.Column(db.String, nullable=False)
    medication=db.Column(db.String, nullable=False)
    medication_response=db.Column(db.String, nullable=False)

    