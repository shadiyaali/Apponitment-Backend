from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import *
from .serializers import *

# ✅ Doctor Views
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def create(self, request, *args, **kwargs):
        """Handles doctor creation with error handling"""
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'Doctor with this email or phone already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_object(self):
        """Handle 404 errors for non-existent doctor"""
        try:
            return super().get_object()
        except NotFound:
            raise NotFound({'error': 'Doctor not found!'})


# ✅ Patient Views
class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        """Handles patient creation with error handling"""
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'Patient with this email or phone already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_object(self):
        """Handle 404 errors for non-existent patient"""
        try:
            return super().get_object()
        except NotFound:
            raise NotFound({'error': 'Patient not found!'})


# ✅ Appointment Views
from django.db.models import Q

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        """Handles appointment creation with validation"""
        doctor = request.data.get("doctor")
        date = request.data.get("date")
        time = request.data.get("time")

        # Check if the doctor already has an appointment at this time
        if Appointment.objects.filter(doctor=doctor, date=date, time=time).exists():
            return Response({'error': 'Doctor is already booked at this time!'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the patient already has an appointment at this time
        patient = request.data.get("patient")
        if Appointment.objects.filter(patient=patient, date=date, time=time).exists():
            return Response({'error': 'Patient already has an appointment at this time!'}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with normal creation
        return super().create(request, *args, **kwargs)



class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:  # Use ID-based serializer for updating
            return AppointmentSerializer
        return AppointmentDetailSerializer  # Use detailed serializer for retrieving

    def get_object(self):
        """Handle 404 errors for non-existent appointment"""
        try:
            return super().get_object()
        except NotFound:
            raise NotFound({'error': 'Appointment not found!'})

