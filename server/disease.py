from patients import db ,Patient


class Disease(db.Model):
    __tablename__ = "disease"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

    treatment=db.relationship('Treatment', backref='disease')

    