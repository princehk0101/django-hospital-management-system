from django.urls import path
from . import views

urlpatterns = [

#  ADMIN 
path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

# Doctors
path('admin/doctors/', views.admin_doctors, name='admin_doctors'),
path('admin/doctors/add/', views.admin_doctors_form, name='admin_doctors_form'),
path('admin/doctors/edit/<int:id>/', views.admin_doctors_edit, name='admin_doctors_edit'),
path('admin/doctors/delete/<int:id>/', views.admin_doctors_delete, name='admin_doctors_delete'),

# Patients
path('admin/patients/', views.admin_patients, name='admin_patients'),
path('admin/patients/add/', views.admin_add_patient, name='admin_add_patient'),
path('admin/patients/edit/<int:id>/', views.admin_edit_patient, name='admin_edit_patient'),
path('admin/patients/delete/<int:id>/', views.admin_delete_patient, name='admin_delete_patient'),

# Appointments
path('admin/appointments/', views.admin_appointments, name='admin_appointments'),
path('admin/appointment/edit/<int:id>/', views.admin_edit_appointment, name='admin_edit_appointment'),
path('admin/appointment/delete/<int:id>/', views.admin_delete_appointment, name='admin_delete_appointment'),

# Search
path('admin/search/', views.admin_search, name='admin_search'),


    #  DOCTOR 
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor/appointments/', views.doctor_appointments, name='doctor_appointments'),
    path('doctor/patient-history/', views.doctor_patient_history, name='doctor_patient_history'),
    path('doctor/treatment/<int:appointment_id>/', views.doctor_treatment_form, name='doctor_treatment_form'),

    path('doctor/availability/', views.doctor_availability, name='doctor_availability'),
    path("doctor/profile/", views.doctor_profile, name="doctor_profile"),
    path("doctor/profile-edit/", views.doctor_profile_edit, name="doctor_profile_edit"),

    # PATIENT 
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient/appointments/', views.patient_appointments, name='patient_appointments'),
    path('patient/book-appointment/', views.patient_book_appointment, name='patient_book_appointment'),
    path('patient/profile/', views.patient_profile, name='patient_profile'),
    path('patient/doctors/', views.patient_doctors_list, name='patient_doctors_list'),

    path('patient/doctor-profile/', views.patient_doctor_profile, name='patient_doctor_profile'),
    path('patient/history/', views.patient_history, name='patient_history'),
    path('patient/profile-edit/', views.patient_profile_edit, name='patient_profile_edit'),


    path('api/doctors/', views.DoctorAPI.as_view(), name='api_doctors'),
]

