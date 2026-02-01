from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

from datetime import date, timedelta

from .models import Doctor, Patient, Appointment, Treatment, Availability

from accounts.decorators import admin_required

# ADMIN PAGES

@admin_required
def admin_dashboard(request):
    total_doctors = Doctor.objects.count()
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()

    return render(request, "admin/dashboard.html", {
        "total_doctors": total_doctors,
        "total_patients": total_patients,
        "total_appointments": total_appointments,
    })



#DOCTORS 
@admin_required
def admin_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, "admin/doctors.html", {"doctors": doctors})

@admin_required
def admin_doctors_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    user = doctor.user  # linked user

    doctor.delete()     # delete doctor record
    user.delete()       # delete user account

    messages.success(request, "Doctor deleted successfully!")
    return redirect("admin_doctors")

@admin_required
def admin_doctors_form(request):
    """Add doctor"""
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        specialization = request.POST["specialization"]
        dept = request.POST["department"]
        exp = request.POST["experience"]
        language = request.POST["language"]
        location = request.POST["location"]

        user = User.objects.create(
            username=fname.lower(),
            first_name=fname,
            last_name=lname
        )

        Doctor.objects.create(
            user=user,
            specialization=specialization,
            experience=exp,
            department=dept,
            language=language,
            location=location
        )

        messages.success(request, "Doctor added successfully!")
        return redirect("admin_doctors")

    return render(request, "admin/doctors_form.html")


# PATIENTS 
@admin_required
def admin_patients(request):
    patients = Patient.objects.all()
    return render(request, "admin/patients.html", {"patients": patients})

@admin_required
def admin_add_patient(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        address = request.POST["address"]
        phone = request.POST["phone"]

        user = User.objects.create(
            username=fname.lower(),
            first_name=fname,
            last_name=lname
        )

        Patient.objects.create(
            user=user,
            age=age,
            gender=gender,
            address=address,
            phone_number=phone
        )

        messages.success(request, "Patient added successfully!")
        return redirect("admin_patients")

    return render(request, "admin/add_patient.html")


# APPOINTMENTS
@admin_required
def admin_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, "admin/appointments.html", {
        "appointments": appointments
    })
@admin_required
def admin_edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        appointment.date = request.POST["date"]
        appointment.time = request.POST["time"]
        appointment.status = request.POST["status"]
        appointment.save()

        messages.success(request, "Appointment updated successfully!")
        return redirect("admin_appointments")

    return render(request, "admin/edit_appointment.html", {
        "appointment": appointment
    })

@admin_required
def admin_delete_appointment(request, id):
    ap = get_object_or_404(Appointment, id=id)
    ap.delete()
    messages.success(request, "Appointment deleted successfully!")
    return redirect("admin_appointments")

@admin_required
def admin_edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        patient.user.first_name = request.POST["fname"]
        patient.user.last_name = request.POST["lname"]
        patient.age = request.POST["age"]
        patient.gender = request.POST["gender"]
        patient.phone_number = request.POST["phone"]
        patient.address = request.POST["address"]

        patient.user.save()
        patient.save()

        messages.success(request, "Patient updated successfully!")
        return redirect("admin_patients")

    return render(request, "admin/edit_patient.html", {"patient": patient})

@admin_required
def admin_delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    user = patient.user
    patient.delete()
    user.delete()
    messages.success(request, "Patient deleted successfully!")
    return redirect("admin_patients")

@admin_required
def admin_doctors_edit(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == "POST":
        doctor.user.first_name = request.POST["fname"]
        doctor.user.last_name = request.POST["lname"]
        doctor.specialization = request.POST["specialization"]
        doctor.department = request.POST["department"]
        doctor.experience = request.POST["experience"]
        doctor.language = request.POST["language"]
        doctor.location = request.POST["location"]

        doctor.user.save()
        doctor.save()

        messages.success(request, "Doctor updated successfully!")
        return redirect("admin_doctors")

    return render(request, "admin/edit_doctor.html", {"doctor": doctor})


@admin_required
def admin_delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()

    messages.success(request, "Appointment deleted successfully!")
    return redirect("admin_appointments")


# ---------- SEARCH ----------
@admin_required
def admin_search(request):
    query = request.GET.get("q", "")

    doctors = Doctor.objects.filter(user__first_name__icontains=query)
    patients = Patient.objects.filter(user__first_name__icontains=query)

    return render(request, "admin/search.html", {
        "doctors": doctors,
        "patients": patients,
        "query": query,
    })



# DOCTOR PAGES


@login_required
def doctor_dashboard(request):
    doctor = Doctor.objects.get(user=request.user)
    today = date.today()

    today_appointments = Appointment.objects.filter(
        doctor=doctor, date=today
    ).order_by("time")

    today_count = today_appointments.count()

    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    week_count = Appointment.objects.filter(
        doctor=doctor,
        date__range=[week_start, week_end]
    ).count()

    working_hours = today_count * 2  

    return render(request, "doctor/dashboard.html", {
        "doctor": doctor,
        "today_appointments": today_appointments,
        "today_count": today_count,
        "week_count": week_count,
        "working_hours": working_hours
    })


@login_required
def doctor_appointments(request):
    doctor = Doctor.objects.get(user=request.user)
    today = date.today()

    appointments = Appointment.objects.filter(
        doctor=doctor,
        date=today
    ).order_by("time")

    return render(request, "doctor/appointments.html", {"appointments": appointments})


@login_required
def doctor_patient_history(request):
    doctor = Doctor.objects.get(user=request.user)
    records = Treatment.objects.filter(appointment__doctor=doctor)

    return render(request, "doctor/patient_history.html", {"records": records})


@login_required
def doctor_treatment_form(request, appointment_id):
    doctor = Doctor.objects.get(user=request.user)
    appointment = Appointment.objects.get(id=appointment_id, doctor=doctor)

    if request.method == "POST":
        diagnosis = request.POST.get("diagnosis")
        prescription = request.POST.get("prescription")
        notes = request.POST.get("notes")

        # Save treatment on existing appointment
        Treatment.objects.create(
            appointment=appointment,
            diagnosis=diagnosis,
            prescription=prescription,
            notes=notes
        )

        # Mark appointment completed
        appointment.status = "Completed"
        appointment.save()

        messages.success(request, "Treatment added successfully!")
        return redirect("doctor_patient_history")

    return render(request, "doctor/treatment_form.html", {"appointment": appointment})



@login_required
def doctor_availability(request):
    doctor = Doctor.objects.get(user=request.user)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if request.method == "POST":
        for day in days:
            value = request.POST.get(day)
            obj, created = Availability.objects.get_or_create(doctor=doctor, day=day)
            obj.time_range = value
            obj.save()

        messages.success(request, "Availability updated!")
        return redirect("doctor_availability")

    availability = {a.day: a.time_range for a in Availability.objects.filter(doctor=doctor)}

    return render(request, "doctor/availability.html", {
        "availability": availability,
        "days": days
    })

@login_required
def doctor_profile(request):
    doctor = Doctor.objects.get(user=request.user)

    return render(request, "doctor/profile.html", {
        "doctor": doctor
    })

@login_required
def doctor_profile_edit(request):
    doctor = Doctor.objects.get(user=request.user)

    if request.method == "POST":
        doctor.user.first_name = request.POST["fname"]
        doctor.user.last_name = request.POST["lname"]
        doctor.specialization = request.POST["specialization"]
        doctor.department = request.POST["department"]
        doctor.experience = request.POST["experience"]
        doctor.language = request.POST["language"]
        doctor.location = request.POST["location"]

        doctor.user.save()
        doctor.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("doctor_profile")

    return render(request, "doctor/profile_edit.html", {
        "doctor": doctor
    })



# PATIENT PAGES


@login_required
def patient_dashboard(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        messages.error(request, "Patient profile does not exist. Please contact admin.")
        return redirect("login")

    doctors = Doctor.objects.all()
    availability = Availability.objects.all()

    upcoming = Appointment.objects.filter(
        patient=patient,
        date__gte=date.today()
    ).order_by("date")

    departments = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics"]

    return render(request, "patient/dashboard.html", {
        "patient": patient,
        "doctors": doctors,
        "availability": availability,
        "upcoming": upcoming,
        "departments": departments,
    })


@login_required
def patient_appointments(request):
    patient = Patient.objects.get(user=request.user)

    upcoming = Appointment.objects.filter(
        patient=patient,
        date__gte=date.today()
    ).order_by("date")

    past = Appointment.objects.filter(
        patient=patient,
        date__lt=date.today()
    ).order_by("-date")

    return render(request, "patient/appointments.html", {
        "upcoming": upcoming,
        "past": past
    })


from .models import Doctor

from datetime import datetime

@login_required
def patient_book_appointment(request):

    departments = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics"]
    doctors = Doctor.objects.all()

    if request.method == "POST":
        dept = request.POST.get("department")
        doctor_id = request.POST.get("doctor")
        date_str = request.POST.get("date")     # string
        time_str = request.POST.get("time")     # string
        symptoms = request.POST.get("symptoms")

        doctor = Doctor.objects.get(id=doctor_id)

        #  Convert string to actual date & time objects
        appointment_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        appointment_time = datetime.strptime(time_str, "%H:%M").time()

        Appointment.objects.create(
            patient=request.user.patient,
            doctor=doctor,
            date=appointment_date,
            time=appointment_time,
            symptoms=symptoms,
            status="Waiting"
        )

        messages.success(request, "Appointment booked successfully!")
        return redirect("patient_appointments")

    return render(request, "patient/book_appointment.html", {
        "departments": departments,
        "doctors": doctors
    })







@login_required
def patient_doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, "patient/doctors_list.html", {"doctors": doctors})


@login_required
def patient_doctor_profile(request):
    doctor_id = request.GET.get("id")

    if not doctor_id:
        messages.error(request, "Doctor ID missing.")
        return redirect("patient_doctors_list")

    doctor = get_object_or_404(Doctor, id=doctor_id)
    availability = Availability.objects.filter(doctor=doctor)

    return render(request, "patient/doctor_profile.html", {
        "doctor": doctor,
        "availability": availability
    })


@login_required
def patient_history(request):
    patient = Patient.objects.get(user=request.user)
    records = Treatment.objects.filter(appointment__patient=patient)

    return render(request, "patient/history.html", {"records": records})


@login_required
def patient_profile(request):
    patient = Patient.objects.get(user=request.user)
    return render(request, "patient/profile.html", {"patient": patient})


@login_required
def patient_profile_edit(request):
    patient = Patient.objects.get(user=request.user)

    if request.method == "POST":
        patient.age = request.POST["age"]
        patient.gender = request.POST["gender"]
        patient.phone_number = request.POST["phone"]
        patient.address = request.POST["address"]
        patient.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("patient_profile")

    return render(request, "patient/profile_edit.html", {"patient": patient})

# API VIEWS

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorAPI(APIView):

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
