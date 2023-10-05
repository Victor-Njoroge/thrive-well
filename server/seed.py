from patients import db, Patient
from disease import Disease
from hospital import Hospital
from next_of_kin import Next_of_kin
from doctor import Doctor
from treatment import Treatment
from appointment import Appointment
from datetime import time, date
from progress import Progress
from sqlalchemy.exc import IntegrityError
from main import app
def seed_data():
    # Create a database session
    with app.app_context():
        with db.session.begin():
            try:
                # Seed Patients
                for i in range(10):
                    patient = Patient(
                        fname=f'Patient{i}',
                        lname=f'Lastname{i}',
                        password=f'password{i}',  # Manually specify passwords
                        email=f'patient{i}@example.com',
                        phone_number=f'123-456-789{i}',
                        regNo=f'P{i}',
                        gender='Male' if i % 2 == 0 else 'Female'
                    )
                    db.session.add(patient)

                # Seed Diseases
                disease1 = Disease(name='Flu')
                disease2 = Disease(name='Cold')
                db.session.add_all([disease1, disease2])

                # Seed Doctors with passwords
                for i in range(10):
                    doctor = Doctor(
                        fname=f'Doctor{i}',
                        lname=f'Lastname{i}',
                        regNo=f'D{i}',
                        email=f'doctor{i}@example.com',
                        phoneNo=f'555-123-456{i}',
                        gender='Male' if i % 2 == 0 else 'Female',
                        hospital_id=1,
                        password=f'password{i}'  # Manually specify passwords
                    )
                    db.session.add(doctor)

                # Seed Hospitals
                hospital1 = Hospital(name='Hospital A', location='Location A', branch_address='Address A')
                hospital2 = Hospital(name='Hospital B', location='Location B', branch_address='Address B')
                db.session.add_all([hospital1, hospital2])

                # Seed Next of Kin
                for i in range(10):
                    next_of_kin = Next_of_kin(
                        fname=f'NextOfKin{i}',
                        lname=f'Lastname{i}',
                        phone_number=f'111-222-333{i}',
                        patient_id=i + 1
                    )
                    db.session.add(next_of_kin)

                # Seed Appointments
                for i in range(10):
                    appointment = Appointment(
                        doctor_id=i + 1,
                        patient_id=i + 1,
                        appointment_date=date(2023, 10, 10),
                        appointment_time=time(10, 0)
                    )
                    db.session.add(appointment)

                # Seed Progress
                for i in range(10):
                    progress = Progress(
                        treatment_id=i + 1,
                        medical_condition='Stable' if i % 2 == 0 else 'Improving',
                        vital_signs='Normal' if i % 2 == 0 else 'Stable',
                        medication='Medicine A' if i % 2 == 0 else 'Medicine B',
                        medication_response='Good' if i % 2 == 0 else 'Excellent'
                    )
                    db.session.add(progress)

                # Seed Treatments
                for i in range(10):
                    treatment = Treatment(
                        patient_id=i + 1,
                        disease_id=i % 2 + 1,
                        hospital_id=i % 2 + 1,
                        doctor_id=i + 1
                    )
                    db.session.add(treatment)

                # Commit the changes
                db.session.commit()

                print('Data seeding completed.')

            except IntegrityError:
                db.session.rollback()
                print("Data already seeded. Skipping...")

if __name__ == '__main__':
    seed_data()
