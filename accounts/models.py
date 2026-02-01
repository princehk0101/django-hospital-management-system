from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('doctor', 'Doctor'),
    ('patient', 'Patient'),
    ('admin', 'Admin'),
)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
