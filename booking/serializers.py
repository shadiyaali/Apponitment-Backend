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
    # Use PrimaryKeyRelatedField for creating appointments
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'

    def validate_patient(self, value):
        if not value:
            raise serializers.ValidationError("Patient cannot be null.")
        return value

class AppointmentDetailSerializer(serializers.ModelSerializer):
    # Use nested serialization for retrieving appointments
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'