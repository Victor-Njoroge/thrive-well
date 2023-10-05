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
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
db.init_app(app)




@app.route('/patients/<string:regNo>', methods=["GET"])
def patients_under_doctor(regNo):
    if request.method == "GET":
        doctor=Doctor.query.filter_by(regNo=regNo).first()
        
        if doctor :
            patients=Appointment.query.filter_by(doctor_id=doctor.id).all()
            patient_data=[{
                'fname': patient.patient.fname,
                'lname': patient.patient.lname,
                'regNo': patient.patient.regNo,
                'phone_number': patient.patient.phone_number,
                'gender':patient.patient.gender
            } for patient in patients]

        return jsonify(patient_data)
            

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

