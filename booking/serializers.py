# serializers.py
from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department', 'email', 'phone', 'employee_type']


class AttendanceSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), required=False)
    date = serializers.DateField(required=False)

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
   
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), required=False)
    doctor = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.filter(employee_type='Doctor'), required=False)

    class Meta:
        model = Appointment
        fields = ['token_number', 'patient', 'doctor', 'date', 'time', 'status']
