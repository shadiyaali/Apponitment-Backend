from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Doctor, Patient, Appointment
from datetime import date, time

# Unit Test for Models
class DoctorModelTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            name="Dr. John Doe",
            specialization="Cardiologist",
            phone="1234567890",
            email="johndoe@example.com"
        )

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. John Doe")
        self.assertEqual(self.doctor.specialization, "Cardiologist")
        self.assertEqual(str(self.doctor), "Dr. John Doe")


class PatientModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            name="Alice Smith",
            age=30,
            gender="Female",
            phone="9876543210",
            email="alice@example.com"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, "Alice Smith")
        self.assertEqual(self.patient.age, 30)
        self.assertEqual(str(self.patient), f"Alice Smith - {self.patient.patient_id}")


class AppointmentModelTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            name="Dr. John Doe",
            specialization="Cardiologist",
            phone="1234567890",
            email="johndoe@example.com"
        )
        self.patient = Patient.objects.create(
            name="Alice Smith",
            age=30,
            gender="Female",
            phone="9876543210",
            email="alice@example.com"
        )
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=date.today(),
            time=time(10, 0),
            status="Booked"
        )

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.patient.name, "Alice Smith")
        self.assertEqual(self.appointment.doctor.name, "Dr. John Doe")
        self.assertEqual(self.appointment.status, "Booked")
        self.assertIsNotNone(self.appointment.token_number)


# Unit Test for API Endpoints
class DoctorAPITestCase(APITestCase):
    def setUp(self):
        self.doctor_data = {
            "name": "Dr. Jane Smith",
            "specialization": "Neurologist",
            "phone": "5555555555",
            "email": "janesmith@example.com"
        }
        self.response = self.client.post("/doctors/", self.doctor_data)

    def test_create_doctor(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 1)
        self.assertEqual(Doctor.objects.get().name, "Dr. Jane Smith")


class PatientAPITestCase(APITestCase):
    def setUp(self):
        self.patient_data = {
            "name": "Bob Williams",
            "age": 40,
            "gender": "Male",
            "phone": "6666666666",
            "email": "bobwilliams@example.com"
        }
        self.response = self.client.post("/patients/", self.patient_data)

    def test_create_patient(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().name, "Bob Williams")


class AppointmentAPITestCase(APITestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            name="Dr. Jane Smith",
            specialization="Neurologist",
            phone="5555555555",
            email="janesmith@example.com"
        )
        self.patient = Patient.objects.create(
            name="Bob Williams",
            age=40,
            gender="Male",
            phone="6666666666",
            email="bobwilliams@example.com"
        )
        self.appointment_data = {
            "patient": self.patient.id,
            "doctor": self.doctor.id,
            "date": str(date.today()),
            "time": "10:00:00",
            "status": "Booked"
        }
        self.response = self.client.post("/appointments/", self.appointment_data)

    def test_create_appointment(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(Appointment.objects.get().status, "Booked")
