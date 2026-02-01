from django.contrib import admin
from .models import Doctor, Patient, Appointment, Treatment, Availability

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Treatment)
admin.site.register(Availability)
