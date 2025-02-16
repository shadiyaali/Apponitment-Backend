# serializers.py
from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department', 'email', 'phone', 'employee_type']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'date', 'is_present']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_id', 'name', 'age', 'gender', 'phone', 'email']
\

class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.filter(employee_type='Doctor'))

    class Meta:
        model = Appointment
        fields = ['token_number', 'patient', 'doctor', 'date', 'time', 'status']




class AppointmentGetSerializer(serializers.ModelSerializer):
    # Use the PatientSerializer for the patient field to get full patient details
    patient = PatientSerializer()
    
    # Use the EmployeeSerializer for the doctor field to get full doctor details
    doctor = EmployeeSerializer()

    class Meta:
        model = Appointment
        fields = ['token_number', 'patient', 'doctor', 'date', 'time', 'status']

