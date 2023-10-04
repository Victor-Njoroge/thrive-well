from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Patient, NextOfKin  # Import your models from models.py
from flask_migrate import Migrate
app = Flask(__name__)

# Configure your database URI here (e.g., SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: Disable tracking modifications

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Create a new patient and their next of kin
@app.route('/patient', methods=['POST'])
def create_patient_and_next_of_kin():
    session = db.session
    data = request.json

    # Gather patient information
    patient = Patient(fname=data['fname'], lname=data['lname'], password=data['password'],
                      email=data['email'], phone_number=data['phone_number'])
    session.add(patient)

    # Gather next of kin information
    next_of_kin = NextOfKin(fname=data['next_of_kin']['fname'], lname=data['next_of_kin']['lname'],
                            phone_number=data['next_of_kin']['phone_number'], patient=patient)
    session.add(next_of_kin)

    session.commit()
    session.close()
    return jsonify({'message': 'Patient and Next of Kin created successfully', 'patient_id': patient.id}), 201

# Retrieve a patient by ID
@app.route('/patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.filter_by(id=patient_id).first()
    if patient:
        return jsonify({'id': patient.id, 'fname': patient.fname, 'lname': patient.lname,
                        'email': patient.email, 'phone_number': patient.phone_number}), 200
    else:
        return jsonify({'error': 'Patient not found'}), 404

# Create tables based on the defined models
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
