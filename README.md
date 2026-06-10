#  Django Hospital Management System

A full-featured Hospital Management System built with **Django** and **MySQL**, designed to streamline the management of doctors, patients, and appointments through a role-based access system.

🔗 **Live Demo:** [https://django-hospital-management-system.onrender.com](https://django-hospital-management-system.onrender.com)

---

##  Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Roles & Access](#roles--access)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Installation & Setup](#installation--setup)
- [Deployment](#deployment)
- [Screenshots](#screenshots)

---

##  Features

###  Admin Panel
- Dashboard with overview statistics
- Add, Edit, Delete **Doctors**
- Add, Edit, Delete **Patients**
- Manage and Edit/Delete **Appointments**
- Search functionality across records

###  Doctor Portal
- Doctor Dashboard
- View assigned appointments
- View patient history
- Fill treatment forms per appointment
- Manage availability schedule
- View and edit personal profile

###  Patient Portal
- Patient Dashboard
- Book new appointments
- View appointment history
- Browse available doctors
- View doctor profiles
- View personal medical history
- Edit own profile

###  Authentication
- Role-based login system (Admin / Doctor / Patient)
- User registration

###  REST API
- Doctor listing and detail via Django REST Framework
- RESTful endpoints under `/api/`

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django (Python) |
| Database | MySQL |
| API | Django REST Framework |
| Frontend | HTML, CSS, Bootstrap |
| Deployment | Render |
| Version Control | Git & GitHub |

---

##  Roles & Access

| Role | Access |
|---|---|
| **Admin** | Full control — manage doctors, patients, appointments |
| **Doctor** | View appointments, patient history, manage availability |
| **Patient** | Book appointments, view history, browse doctors |

---

##  Project Structure

```
django-hospital-management-system/
│
├── Hospital_Management_System/   # Main Django project settings
├── accounts/                     # Auth: login, register, home, contact
├── hospital/                     # Core app: doctors, patients, appointments
├── static/                       # Static files (CSS, JS, images)
│
├── manage.py
├── requirements.txt
├── build.sh                      # Render build script
├── start.sh                      # Render start script
└── README.md
```

---

##  URL Routes

### Public Routes (`accounts` app)
| URL | View | Description |
|---|---|---|
| `/` | home | Home page |
| `/login/` | login | Login page |
| `/register/` | register | Registration page |
| `/contact/` | contact | Contact page |
| `/about/` | about | About page |

### Admin Routes
| URL | Description |
|---|---|
| `/admin/dashboard/` | Admin dashboard |
| `/admin/doctors/` | List all doctors |
| `/admin/doctors/add/` | Add new doctor |
| `/admin/doctors/edit/<id>/` | Edit doctor |
| `/admin/doctors/delete/<id>/` | Delete doctor |
| `/admin/patients/` | List all patients |
| `/admin/patients/add/` | Add new patient |
| `/admin/search/` | Search records |

### Doctor Routes
| URL | Description |
|---|---|
| `/doctor/dashboard/` | Doctor dashboard |
| `/doctor/appointments/` | View appointments |
| `/doctor/patient-history/` | Patient history |
| `/doctor/treatment/<id>/` | Treatment form |
| `/doctor/availability/` | Set availability |
| `/doctor/profile/` | View profile |

### Patient Routes
| URL | Description |
|---|---|
| `/patient/dashboard/` | Patient dashboard |
| `/patient/book-appointment/` | Book appointment |
| `/patient/appointments/` | View appointments |
| `/patient/doctors/` | Browse doctors |
| `/patient/history/` | Medical history |
| `/patient/profile/` | View profile |

---

##  API Endpoints

Base URL: `/api/`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/<id>/` | Get doctor detail |
| POST | `/api/doctors/` | Create doctor |
| PUT | `/api/doctors/<id>/` | Update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

> Built using **Django REST Framework** with a `DefaultRouter`.

---

##  Installation & Setup

### Prerequisites
- Python 3.10+
- MySQL Server
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/princehk0101/django-hospital-management-system.git
cd django-hospital-management-system

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure database
# Open Hospital_Management_System/settings.py and update DATABASES:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 5. Apply migrations
python manage.py migrate

# 6. Create superuser (Admin)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  Deployment

This project is deployed on **Render**.

- `build.sh` — installs dependencies and runs migrations on Render
- `start.sh` — starts the Gunicorn server

**Environment Variables required on Render:**
```
SECRET_KEY=your_secret_key
DEBUG=False
DATABASE_URL=your_mysql_connection_string
ALLOWED_HOSTS=your-render-domain.onrender.com
```

---

##  Author

**Chhotelal Chauhan** ([@princehk0101](https://github.com/princehk0101))
>  Built as a **personal learning project** to practice Django, MySQL, REST API, and cloud deployment.

---


