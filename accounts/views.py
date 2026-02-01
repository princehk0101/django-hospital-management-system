from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from hospital.models import Doctor, Patient
from django.contrib import messages



#   USER REGISTER

from accounts.models import Account
from hospital.models import Doctor, Patient

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if User.objects.filter(username=email).exists():
            return render(request, "register.html", {"error": "Email already registered!"})

        fname = name.split(" ")[0]
        lname = " ".join(name.split(" ")[1:])

        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=fname,
            last_name=lname,
            password=password
        )

        acc = Account.objects.create(
            user=user,
            phone=phone,
            role=role
        )

        if role == "doctor":
            Doctor.objects.create(
                user=user,
                specialization="",
                department="",
                experience=0,
                language="",
                location=""
            )
        elif role == "patient":
            Patient.objects.create(
                user=user,
                age=0,
                gender="",
                address="",
                phone_number=phone
            )

        return redirect("login")

    return render(request, "register.html")






# LOGIN

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role").lower()   # lower here

        # Try authenticate using username directly
        user = authenticate(username=email, password=password)

        if not user:
            try:
                u = User.objects.get(email=email)
                user = authenticate(username=u.username, password=password)
            except:
                user = None

        if not user:
            return render(request, "login.html", {"error": "Invalid email or password!"})

        #  ADMIN LOGIN — skip Account model
        if role == "admin":
            if not user.is_superuser:
                return render(request, "login.html", {"error": "You are not an admin!"})

            auth_login(request, user)
            return redirect("/hospital/admin/dashboard/")

        #  DOCTOR & PATIENT LOGIN — must exist in Account model
        try:
            acc = Account.objects.get(user=user)
        except:
            return render(request, "login.html", {"error": "Account not found!"})

        if acc.role.lower() != role:   # lowercase compare
            return render(request, "login.html", {"error": "Role does not match!"})

        auth_login(request, user)

        if role == "doctor":
            return redirect("/hospital/doctor/dashboard/")
        elif role == "patient":
            return redirect("/hospital/patient/dashboard/")

    return render(request, "login.html")








def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')



def about(request):
    return render(request, 'about.html')