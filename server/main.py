from patients import db, Patient
from disease import Disease
from hospital import Hospital
from next_of_kin import Next_of_kin
from doctor import Doctor
from treatment import Treatment
from appointment import Appointment
from progress import Progress
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
app = Flask(__name__)
gunicorn app:app
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://thrivewell_user:IkonmnWbPZYcMACv2hFXufZWLnPrYgda@dpg-ckdvee4iibqc73b2u63g-a.oregon-postgres.render.com/thrivewell'
db.init_app(app)




@app.route('/patient', methods=["GET"])
def patients_under_doctor():
    if request.method == "GET":
        patients=Patient.query.all()
        patient_list = []

        for patient in patients:
            patient_info = {
                'id': patient.id,
                'fname': patient.fname,
                'lname': patient.lname,
                'email': patient.email,
                'phone_number': patient.phone_number,
                'regNo': patient.regNo,
                'gender': patient.gender
            }
            patient_list.append(patient_info)

        return jsonify({'patients': patient_list})
            
@app.route('/doctor', methods=["GET"])
def all_doctors():
    if request.method == "GET":
        doctors = Doctor.query.all()
        doctor_list = []

       
        for doctor in doctors:
            doctor_info = {
                'id': doctor.id,
                'fname': doctor.fname,
                'lname': doctor.lname,
                'regNo': doctor.regNo,
                'email': doctor.email,
                'phoneNo': doctor.phoneNo,
                'gender': doctor.gender,
                'hospital_id': doctor.hospital_id
            }
            doctor_list.append(doctor_info)
        return jsonify({'doctors': doctor_list})

@app.route('/progress/<string:regNo>', methods=["GET"])
def patients_progress(regNo):
    if request.method == "GET":
        patient = Patient.query.filter_by(regNo=regNo).first()

        if patient:
            treatments = Treatment.query.filter_by(patient_id=patient.id).all()
            progress_data = []
            for treatment in treatments:
                progress = Progress.query.filter_by(treatment_id=treatment.id).first()
                if progress:
                    progress_data.append({
                        'treatment_id': treatment.id,
                        'medical_condition': progress.medical_condition,
                        'vital_signs': progress.vital_signs,
                        'medication': progress.medication,
                        'medication_response': progress.medication_response
                    })

            return jsonify(progress_data)
        else:
            return "Patient not found", 404

@app.route('/appointments', methods=["GET"])
def all_appointments():
    if request.method == "GET":
        appointments = Appointment.query.all()
        appointment_list = []

        for appointment in appointments:
            doctor = Doctor.query.get(appointment.doctor_id)
            patient = Patient.query.get(appointment.patient_id)
            appointment_dict = {
                'id': appointment.id,
                'doctor_regNo': doctor.regNo if doctor else None,  
                'patient_regNo': patient.regNo if patient else None,  
                'appointment_date': appointment.appointment_date.strftime('%Y-%m-%d'),
                'appointment_time': appointment.appointment_time.strftime('%H:%M:%S')
            }

            appointment_list.append(appointment_dict)
        return jsonify(appointment_list)

@app.route('/update_appointment/<int:id>', methods=["PATCH"])
def update_appointment_date(id):
    if request.method == "PATCH":
        try:
            data = request.json
            appointment = Appointment.query.filter_by(id=id).first()

            if appointment:
                new_date_str = data.get('appointment_date')
                new_date = datetime.strptime(new_date_str, '%Y-%m-%d').date()  # Convert the string to a date object
                appointment.appointment_date = new_date

                db.session.commit()
                return jsonify({"message": "Appointment date updated successfully"})
            else:
                return jsonify({"error": "Appointment not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 
       












@app.route('/update_progress/<string:regNo>', methods=["PATCH"])
def update_progress(regNo):
    if request.method == "PATCH":
        
        
        patient = Patient.query.filter_by(regNo=regNo).first()

        if patient:
            
            data = request.get_json()

            
            if 'treatment_id' in data and 'medical_condition' in data and 'vital_signs' in data and 'medication' in data and 'medication_response' in data:
                
          
                treatment = Treatment.query.filter_by(patient_id=patient.id, id=data['treatment_id']).first()

                if treatment:
                    
                    progress = Progress.query.filter_by(treatment_id=treatment.id).first()
                    if not progress:
                        progress = Progress(
                            treatment_id=treatment.id,
                            medical_condition=data['medical_condition'],
                            vital_signs=data['vital_signs'],
                            medication=data['medication'],
                            medication_response=data['medication_response']
                        )
                        db.session.add(progress)
                    else:
                        
                        progress.medical_condition = data['medical_condition']
                        progress.vital_signs = data['vital_signs']
                        progress.medication = data['medication']
                        progress.medication_response = data['medication_response']

                   
                    db.session.commit()
                    return "Progress updated successfully"
                else:
                    return "Treatment not found for this patient", 404
            else:
                return "Required fields missing in the request data", 400
        else:
            return "Patient not found", 404

doctor_credentials = {
    "regNo": "th4971",
    "password": "samplepassword"  # You should securely hash and store passwords in your database
}

@app.route('/create_patient', methods=["POST"])
def post_patient():
    if request.method == "POST":
        data = request.json  # Get JSON data directly

        print("Received Data:", data)

        if 'fname' in data and 'lname' in data and 'password' in data and 'email' in data and 'phone_number' in data and 'regNo' in data and 'gender' in data:
            new_patient = Patient(
                fname=str(data['fname']), 
                lname=str(data['lname']),  
                password=str(data['password']), 
                email=str(data['email']),  
                phone_number=str(data['phone_number']), 
                regNo=str(data['regNo']),  
                gender=str(data['gender'])
            )

            db.session.add(new_patient)
            db.session.commit()

            return jsonify({'message': 'Patient created successfully'}), 201
        else:
            return jsonify({'error': 'Missing fields in the request data'}), 400


@app.route('/create_doctor', methods=["POST"])
def post_doctor():
    if request.method == "POST":
        data = request.json

        print("Received Data:", data)

        if 'fname' in data and 'lname' in data and 'password' in data and 'email' in data and 'phone_number' in data and 'regNo' in data and 'gender' in data:
            new_doctor = Doctor(
                fname=str(data['fname']),
                lname=str(data['lname']),
                password=str(data['password']),
                email=str(data['email']),
                phoneNo=str(data['phone_number']),
                regNo=str(data['regNo']),
                gender=str(data['gender'])
            )

            db.session.add(new_doctor)
            db.session.commit()

            return jsonify({'message': 'Doctor created successfully'}), 201
        else:
            return jsonify({'error': 'Missing fields in the request data'}), 400


@app.route('/get_treatments', methods=["GET"])
def get_treatments():
    try:
        treatments = Treatment.query.all()
        treatments_list = []

        for treatment in treatments:
            patient = Patient.query.get(treatment.patient_id)
            doctor = Doctor.query.get(treatment.doctor_id)

            treatment_dict = {
                'id': treatment.id,
                'patient_regNo': patient.regNo if patient else None,
                'doctor_regNo': doctor.regNo if doctor else None,
                'disease_id': treatment.disease_id,
                'hospital_id': treatment.hospital_id,
            }

            treatments_list.append(treatment_dict)

        return jsonify({'treatments': treatments_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/update_treatment_progress', methods=['PATCH'])
def update_treatment_progress():
    data = request.get_json()

   
    patient_regNo = data.get('patient_regNo')
    doctor_regNo = data.get('doctor_regNo')
    new_progress = data.get('progress') 

    patient = Patient.query.filter_by(regNo=patient_regNo).first()
    doctor = Doctor.query.filter_by(regNo=doctor_regNo).first()

    if not patient or not doctor:
        return jsonify({'message': 'Patient or doctor not found'}), 404

    treatment = Treatment.query.filter_by(
        patient_id=patient.id,
        doctor_id=doctor.id
    ).first()

    if not treatment:
        return jsonify({'message': 'Treatment not found'}), 404

    
    treatment.progress = new_progress

    db.session.commit()

    return jsonify({'message': 'Treatment progress updated successfully'})


@app.route('/login_doctor', methods=["POST"])
def doctor_login():
    data = request.get_json()
    if 'regNo' in data and 'password' in data:
        regNo = data['regNo']
        password = data['password']
        doctor = Doctor.query.filter_by(regNo=regNo).first()
        if doctor:
            if doctor.password == password:
                appointments_data = doctor_appointments(regNo)
                response_data = {
                    'message': 'Doctor logged in successfully',
                    'appointments': appointments_data
                }
                return jsonify(response_data), 200
            else:
                return jsonify({'error': 'Invalid password'}), 401
        else:
            return jsonify({'error': 'Doctor not found'}), 404
    else:
        return jsonify({'error': 'Missing regNo or password in the request data'}), 400


@app.route(f'/appointment/<string:regNo>', methods=["GET"])
def doctor_appointments(regNo):
    if request.method == "GET":
        doctor = Doctor.query.filter_by(regNo=regNo).first()
        if doctor:
            appointments = Appointment.query.filter_by(doctor_id=doctor.id).all()
            appointments_data = [{
                'fname': appointment.patient.fname,
                'lname': appointment.patient.lname,
                'regNo': appointment.patient.regNo,
                'phone_number': appointment.patient.phone_number,
                'appointment_date': appointment.appointment_date.strftime('%Y-%m-%d'),
                'appointment_time': appointment.appointment_time.strftime('%H:%M:%S')
            } for appointment in appointments]
            return jsonify(appointments_data)
        else:
            return jsonify({'error': 'Doctor not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)

