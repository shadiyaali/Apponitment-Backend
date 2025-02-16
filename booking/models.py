from django.db import models
import random


class Employee(models.Model):
    DOCTOR = 'Doctor'
    NURSE = 'Nurse'

    EMPLOYEE_TYPES = [
        (DOCTOR, 'Doctor'),
        (NURSE, 'Nurse'),
    ]

    name = models.CharField(max_length=200,null=True, blank=True)
    department = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(unique=True,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    employee_type = models.CharField(
        max_length=10,
        choices=EMPLOYEE_TYPES,
        default=DOCTOR,
    )

    def __str__(self):
        return f'{self.name} ({self.get_employee_type_display()})'


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=True)   
   
    class Meta:
        unique_together = ('employee', 'date')   

    def __str__(self):
        return f'{self.employee.name} - {self.date} - {"Present" if self.is_present else "Absent"}'
    


class Patient(models.Model):
    patient_id = models.PositiveIntegerField(unique=True, editable=False, null=True,blank =True)
    name = models.CharField(max_length=255,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')],null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
   
        if not self.patient_id:
            while True:
                new_id = random.randint(10000, 99999)  
                if not Patient.objects.filter(patient_id=new_id).exists():   
                    self.patient_id = new_id
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.patient_id}"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('Pending', 'Pending'),
        ('Checked In', 'Checked In'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    token_number = models.PositiveIntegerField(unique=True, editable=False, null=True, blank=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey('Employee', on_delete=models.CASCADE, limit_choices_to={'employee_type': 'Doctor'}, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        if not self.token_number:
            last_appointment = Appointment.objects.order_by('-token_number').first()
            if last_appointment:
                self.token_number = last_appointment.token_number + 1
            else:
                self.token_number = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Token {self.token_number}: {self.patient.name} - {self.doctor.name} - {self.status}"