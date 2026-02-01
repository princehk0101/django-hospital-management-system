from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    experience = models.IntegerField()
    language = models.CharField(max_length=150)
    location = models.CharField(max_length=150)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()}"


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.get_full_name()

class Appointment(models.Model):

    STATUS_CHOICES = (
        ("Waiting", "Waiting"),
        ("In Process", "In Process"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    symptoms = models.TextField(blank=True, null=True)   

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Waiting")

    def __str__(self):
        return f"{self.date} - {self.patient.user.get_full_name()}"



class Treatment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    prescription = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f"Treatment for {self.appointment.patient.user.get_full_name()}"


class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    time_range = models.CharField(max_length=100)   

    def __str__(self):
        return f"{self.doctor} - {self.day}"

