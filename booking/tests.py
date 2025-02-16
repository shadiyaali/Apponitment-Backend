from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee, Patient, Appointment, Attendance
from django.utils import timezone
from datetime import timedelta


class EmployeeTests(APITestCase):

    def setUp(self):
        self.employee_data = {
            'name': 'Dr. John Doe',
            'department': 'Cardiology',
            'email': 'johndoe@example.com',
            'phone': '1234567890',
            'employee_type': 'Doctor'
        }
        self.employee = Employee.objects.create(**self.employee_data)

    def test_create_employee(self):
        response = self.client.post('/employees/', self.employee_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employee(self):
        response = self.client.get(f'/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.employee.name)


class AttendanceTests(APITestCase):

    def setUp(self):
        self.employee = Employee.objects.create(
            name='Dr. Jane Doe',
            department='Surgery',
            email='janedoe@example.com',
            phone='9876543210',
            employee_type='Doctor'
        )
        self.attendance_data = {
            'employee': self.employee.id,
            'date': timezone.now().date(),
            'is_present': True
        }

    def test_create_attendance(self):
        response = self.client.post('/attendance/', self.attendance_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_attendance(self):
        self.client.post('/attendance/', self.attendance_data, format='json')
        response = self.client.post('/attendance/', self.attendance_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PatientTests(APITestCase):

    def setUp(self):
        self.patient_data = {
            'name': 'Alice Smith',
            'age': 30,
            'gender': 'Female',
            'phone': '555-5555',
            'email': 'alice.smith@example.com'
        }

    def test_create_patient(self):
        response = self.client.post('/patients/', self.patient_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_patient(self):
        self.client.post('/patients/', self.patient_data, format='json')
        response = self.client.post('/patients/', self.patient_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AppointmentTests(APITestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            name='Bob Johnson',
            age=40,
            gender='Male',
            phone='555-0000',
            email='bob.johnson@example.com'
        )
        self.employee = Employee.objects.create(
            name='Dr. Sarah Lee',
            department='Orthopedics',
            email='sarahlee@example.com',
            phone='555-9999',
            employee_type='Doctor'
        )
        self.appointment_data = {
            'patient': self.patient.id,
            'doctor': self.employee.id,
            'date': timezone.now().date() + timedelta(days=1),
            'time': '10:00:00',
            'status': 'Booked'
        }

    def test_create_appointment(self):
        response = self.client.post('/appointments/', self.appointment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_appointment_with_past_date(self):
        self.appointment_data['date'] = timezone.now().date() - timedelta(days=1)
        response = self.client.post('/appointments/', self.appointment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Appointment date cannot be in the past.', str(response.data))

    def test_appointment_double_booking(self):
        self.client.post('/appointments/', self.appointment_data, format='json')
        response = self.client.post('/appointments/', self.appointment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('The doctor is already booked at this time.', str(response.data))


class EmployeeCountTodayTests(APITestCase):

    def setUp(self):
        self.employee = Employee.objects.create(
            name='Dr. Emma Stone',
            department='Pediatrics',
            email='emmastone@example.com',
            phone='555-1111',
            employee_type='Doctor'
        )
        self.attendance_data = {
            'employee': self.employee.id,
            'date': timezone.now().date(),
            'is_present': True
        }
        Attendance.objects.create(**self.attendance_data)

    def test_employee_count_today(self):
        response = self.client.get('/employee-count-today/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['doctor_count_today'], 1)
        self.assertEqual(response.data['total_employees_today'], 1)


class AppointmentTodayTests(APITestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            name='Claire Rogers',
            age=50,
            gender='Female',
            phone='555-4444',
            email='claire.rogers@example.com'
        )
        self.employee = Employee.objects.create(
            name='Dr. Adam West',
            department='Neurology',
            email='adamwest@example.com',
            phone='555-2222',
            employee_type='Doctor'
        )
        self.appointment_data = {
            'patient': self.patient.id,
            'doctor': self.employee.id,
            'date': timezone.now().date(),
            'time': '12:00:00',
            'status': 'Booked'
        }
        self.appointment = Appointment.objects.create(**self.appointment_data)

    def test_appointment_today(self):
        response = self.client.get('/appointments-today/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['token_number'], self.appointment.token_number)


class AppointmentOddStatusCountTests(APITestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            name='David Wilson',
            age=60,
            gender='Male',
            phone='555-3333',
            email='david.wilson@example.com'
        )
        self.employee = Employee.objects.create(
            name='Dr. Jessica Brown',
            department='Dermatology',
            email='jessicabrown@example.com',
            phone='555-7777',
            employee_type='Doctor'
        )
        self.appointment_data = {
            'patient': self.patient.id,
            'doctor': self.employee.id,
            'date': timezone.now().date(),
            'time': '14:00:00',
            'status': 'Pending'
        }
        self.appointment = Appointment.objects.create(**self.appointment_data)

    def test_appointment_odd_status_count(self):
        response = self.client.get('/appointment-odd-status-count/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Pending', response.data)
        self.assertIn('Completed', response.data)
        self.assertIn('Cancelled', response.data)
