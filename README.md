#  Task Manager 

A secure and scalable **Task Manager REST API** built using **Django** and **Django REST Framework (DRF)**. This project provides JWT-based authentication, allowing users to securely register, log in, and manage their own tasks through RESTful APIs.

The API ensures that every authenticated user can create, view, update, and delete only their own tasks.

#  Features

### Authentication
- User Registration
- User Login using JWT Authentication
- Access Token & Refresh Token
- Secure API Authorization

### Task Management
- Create Task
- List Tasks
- Retrieve Single Task
- Update Task
- Delete Task

### Authorization
- Users can access only their own tasks.
- Protected API endpoints using JWT Authentication.

### Database
- SQLite Database

### Bonus Features
- Pagination
- Filtering by Task Status

---

# Tech Stack

| Technology | Purpose |

Python - Programming Language 
Django - Backend Framework 
Django REST Framework, REST API Development 
SQLite - Database 
JWT (Simple JWT) - Authentication 
Postman - API Testing 
Django Admin - Database Management 

---

# 📂 Project Structure

```text
task_manager_api/
│
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tasks/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Naveen44555/Task-Manager.git
```

Github User name : https://github.com/Naveen44555
```

## 2. Navigate to the Project

```bash
cd task_manager_api
```

---

## 3. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## 6. Create Superuser

```bash
python manage.py createsuperuser
```

Enter:

- Username
- Email
- Password

---

## 7. Run the Server

```bash
python manage.py runserver
```

Server starts at:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Authentication

This project uses **JWT Authentication**.

### Login Endpoint

```http
POST /api/auth/login/
```

Example Request

```json
{
    "username":"naveen",
    "password":"password123"
}
```

Response

```json
{
    "refresh":"<refresh_token>",
    "access":"<access_token>"
}
```

Copy the **Access Token**.

In Postman:

Authorization

```
Bearer Token
```

Paste the Access Token.

---

# 📌 API Endpoints

## User Registration

```http
POST /api/auth/register/
```

---

## User Login

```http
POST /api/auth/login/
```

---

## Refresh Token

```http
POST /api/auth/refresh/
```

---

## Create Task

```http
POST /api/auth/tasks/create/
```

---

## List Tasks

```http
GET /api/auth/tasks/
```

---

## Retrieve Task

```http
GET /api/auth/tasks/<id>/
```

Example

```http
GET /api/auth/tasks/5/
```

---

## Update Task

```http
PUT /api/auth/tasks/<id>/update/
```

or

```http
PATCH /api/auth/tasks/<id>/update/
```

---

## Delete Task

```http
DELETE /api/auth/tasks/<id>/delete/
```

---

# ⭐ Pagination

Get First Page

```http
GET /api/auth/tasks/
```

Get Second Page

```http
GET /api/auth/tasks/?page=2
```

---

# ⭐ Filtering

Completed Tasks

```http
GET /api/auth/tasks/?status=true
```

Pending Tasks

```http
GET /api/auth/tasks/?status=false
```

---

# 🗄 Database

Database Used

```
SQLite
```

Django Admin URL

```text
http://127.0.0.1:8000/admin/
```

---

# 🧪 API Testing

The APIs were tested using

- Postman

Verified Operations

- User Registration
- Login
- Create Task
- List Tasks
- Retrieve Task
- Update Task
- Delete Task
- Pagination
- Filtering

---

# 🔒 Permissions

- JWT Authentication is required.
- Users can access only their own tasks.
- Unauthorized users cannot access protected endpoints.

---

# 📦 Requirements

Install all dependencies using

```bash
pip install -r requirements.txt
```

---

# 👨‍💻 Author

**Naveen**

GitHub:
https://github.com/Naveen44555

LinkedIn:
https://www.linkedin.com/in/naveen-parthanaboina/

---

# 📄 License

This project was developed as part of a Django REST Framework assessment for learning and evaluation purposes.