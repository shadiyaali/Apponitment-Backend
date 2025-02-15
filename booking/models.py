from django.db import models
import random

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    phone = models.CharField(max_length=20,null = True, blank =True)
    email = models.EmailField(unique=True,null = True, blank =True)

    def __str__(self):
        return self.name



class Patient(models.Model):
    patient_id = models.PositiveIntegerField(unique=True, editable=False, null=True,blank =True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
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
        ('Checked In', 'Checked In'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    token_number = models.PositiveIntegerField(unique=True, editable=False,null=True, blank=True) 
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Booked')

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
