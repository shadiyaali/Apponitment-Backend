from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)  
    doctor_name = serializers.ReadOnlyField(source='doctor.name')

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'doctor_name', 'token_number', 'date', 'time', 'status']