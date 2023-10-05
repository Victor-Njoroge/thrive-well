from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Patient, NextOfKin, db  # Import your models from models.py

app = Flask(__name__)

# Configure your database URI here (e.g., SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: Disable tracking modifications

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create a new patient and their next of kin
@app.route('/patient', methods=['POST'])
def create_patient_and_next_of_kin():
    data = request.json

    # Gather patient information
    patient = Patient(
        fname=data['fname'], lname=data['lname'], password=data['password'],
        email=data['email'], phone_number=data['phone_number']
    )

    # Gather next of kin information
    next_of_kin = NextOfKin(
        fname=data['next_of_kin']['fname'], lname=data['next_of_kin']['lname'],
        phone_number=data['next_of_kin']['phone_number'], patient=patient
    )

    # Add and commit both patient and next_of_kin
    try:
        db.session.add(patient)
        db.session.add(next_of_kin)
        db.session.commit()
        return jsonify({
            'message': 'Patient and Next of Kin created successfully',
            'patient': {
                'id': patient.id,
                'fname': patient.fname,
                'lname': patient.lname,
                'email': patient.email,
                'phone_number': patient.phone_number
            },
            'next_of_kin': {
                'id': next_of_kin.id,
                'fname': next_of_kin.fname,
                'lname': next_of_kin.lname,
                'phone_number': next_of_kin.phone_number
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while creating the patient'}), 500
    finally:
        db.session.close()

# Retrieve a patient and their next of kin by ID
@app.route('/patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.filter_by(id=patient_id).first()
    next_of_kin = NextOfKin.query.filter_by(patient_id=patient_id).first()

    if patient:
        response = {
            'patient': {
                'id': patient.id,
                'fname': patient.fname,
                'lname': patient.lname,
                'email': patient.email,
                'phone_number': patient.phone_number
            },
            'next_of_kin': None
        }

        if next_of_kin:
            response['next_of_kin'] = {
                'id': next_of_kin.id,
                'fname': next_of_kin.fname,
                'lname': next_of_kin.lname,
                'phone_number': next_of_kin.phone_number
            }

        return jsonify(response), 200
    else:
        return jsonify({'error': 'Patient not found'}), 404

# Delete a patient and their next of kin by ID
# Commented out as per request from Victor
# @app.route('/patient/<int:patient_id>', methods=['DELETE'])
# def delete_patient(patient_id):
#     patient = Patient.query.get(patient_id)
#
#     if patient:
#         next_of_kin = NextOfKin.query.filter_by(patient_id=patient_id).first()
#         db.session.delete(patient)
#         if next_of_kin:
#             db.session.delete(next_of_kin)
#         db.session.commit()
#         return jsonify({'message': 'Patient and Next of Kin deleted successfully'}), 200
#     else:
#         return jsonify({'error': 'Patient not found'}), 404

# Create tables based on the defined models
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
