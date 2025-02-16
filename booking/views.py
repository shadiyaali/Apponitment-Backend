# views.py
 
from .models import *
from .serializers import *
from django.utils import timezone
from django.core.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.views import APIView
from datetime import date

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

 
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceListCreate(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
 
        employee = request.data.get('employee')
        date = request.data.get('date')

        if Attendance.objects.filter(employee=employee, date=date).exists():
        
            return Response({
                "non_field_errors": ["Attendance record for this employee already exists on this date."]
            }, status=status.HTTP_400_BAD_REQUEST)

      
        return super().create(request, *args, **kwargs)

class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def update(self, request, *args, **kwargs):
        partial = True  
        instance = self.get_object()
        
         
        data = request.data.copy()
        data.setdefault('employee', instance.employee.id)
        data.setdefault('date', instance.date)
        
  
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
       
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
      
        try:
            return super().get_object()
        except NotFound:
            raise NotFound({'error': 'Patient not found!'})

 

 
 


 

class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data

       
        if data['date'] < timezone.now().date():
            raise ValidationError("Appointment date cannot be in the past.")

       
        if Appointment.objects.filter(doctor=data['doctor'], date=data['date'], time=data['time']).exists():
            raise ValidationError("The doctor is already booked at this time.")
        
        
        if Appointment.objects.filter(patient=data['patient'], date=data['date'], time=data['time']).exists():
            raise ValidationError("The patient already has an appointment at this time.")
        
       
        if not Attendance.objects.filter(employee=data['doctor'], date=data['date'], is_present=True).exists():
            raise ValidationError(f"The doctor {data['doctor'].name} is not present on {data['date']}.")
 
        serializer.save()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)





class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentGetSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        data = serializer.validated_data
        
       
        date = data.get('date', instance.date)

      
        time = data.get('time', instance.time)
   
        if date < timezone.now().date():
            raise ValidationError("Appointment date cannot be in the past.")

      
        patient = data.get('patient', instance.patient)
        doctor = data.get('doctor', instance.doctor)

     
        if Appointment.objects.filter(doctor=doctor, date=date, time=time).exclude(id=instance.id).exists():
            raise ValidationError("The doctor is already booked at this time.")

        if Appointment.objects.filter(patient=patient, date=date, time=time).exclude(id=instance.id).exists():
            raise ValidationError("The patient already has an appointment at this time.")
        
        
        serializer.save()

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)



 

class EmployeeCountTodayView(APIView):
    def get(self, request):
     
        today = date.today()

        
        total_employees_today = Attendance.objects.filter(date=today, is_present=True).count()

     
        doctor_count_today = Attendance.objects.filter(
            employee__employee_type=Employee.DOCTOR, 
            date=today, 
            is_present=True
        ).count()

    
        nurse_count_today = Attendance.objects.filter(
            employee__employee_type=Employee.NURSE, 
            date=today, 
            is_present=True
        ).count()
 
        data = {
            'total_employees_today': total_employees_today,
            'doctor_count_today': doctor_count_today,
            'nurse_count_today': nurse_count_today,
        }
        
        return Response(data)


 

class AppointmentTodayView(APIView):
    def get(self, request):
      
        today = date.today()

      
        appointments_today = Appointment.objects.filter(date=today)
 
        appointments_data = []
        for appointment in appointments_today:
            appointments_data.append({
                'token_number': appointment.token_number,
                'patient': {
                    'id': appointment.patient.id,
                    'name': appointment.patient.name,
                    'age': appointment.patient.age,
                    'gender': appointment.patient.gender,
                    'phone': appointment.patient.phone,
                    'email': appointment.patient.email,
                },
                'doctor': {
                    'id': appointment.doctor.id,
                    'name': appointment.doctor.name,
                    'department': appointment.doctor.department,
                    'email': appointment.doctor.email,
                    'phone': appointment.doctor.phone,
                },
                'date': appointment.date,
                'time': appointment.time,
                'status': appointment.status,
            })

    
        return Response(appointments_data)
    
 

 
class AppointmentOddStatusCountView(APIView):
    def get(self, request):
  
        today = date.today()

     
        appointments_today = Appointment.objects.filter(date=today)

     
        pending_count = appointments_today.filter(status='Pending')
        completed_count = appointments_today.filter(status='Completed')
        cancelled_count = appointments_today.filter(status='Cancelled')

     
        pending_count = pending_count.filter(token_number__in=[a.token_number for a in pending_count if a.token_number % 2 != 0])
        completed_count = completed_count.filter(token_number__in=[a.token_number for a in completed_count if a.token_number % 2 != 0])
        cancelled_count = cancelled_count.filter(token_number__in=[a.token_number for a in cancelled_count if a.token_number % 2 != 0])

       
        status_counts = {
            'Pending ': pending_count.count(),
            'Completed  ': completed_count.count(),
            'Cancelled  ': cancelled_count.count(),
        }

      
        return Response(status_counts)

