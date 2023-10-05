from patients import db

class Hospital(db.Model):
    __tablename__ = 'hospital'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    location=db.Column(db.String, nullable=False)
    branch_address=db.Column(db.String, nullable=False)

    treatment=db.relationship('Treatment', backref='hospital')
    doctor=db.relationship('Doctor',backref='hospital')
    