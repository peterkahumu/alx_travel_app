# 🚀 ALX Travel App — Backend API

This is the backend of the ALX Travel App built with Django REST Framework. It includes listings functionality, REST API, Swagger docs, and environment-based configuration.

---

## 📦 Tech Stack

- Python 3.11+
- Django 5.2
- Django REST Framework
- MySQL
- drf-yasg (Swagger docs)
- django-environ
- CORS support

---

## ⚙️ Setup Instructions

### 1. 🔁 Clone the Repo
```bash
git clone https://github.com/your-username/alx-travel-app.git
cd alx-travel-app
````

### 2. 🧪 Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. 📄 Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the **project root** (same level as `manage.py`) and configure:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```

**Note:** Never commit `.env` to version control.

---

## 🧵 Database Setup

Make sure you have a MySQL database created.

Then run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Create Superuser

```bash
python manage.py createsuperuser
```

---

## 🚀 Run the Server

```bash
python manage.py runserver
```

Visit:

* API Root: [http://localhost:8000/](http://localhost:8000/)
* Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
* Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🌐 CORS Whitelist

The app currently allows frontend devs to connect via:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
]
```

You can update this in `settings.py`.

---

## 📁 Project Structure (Simplified)

```
alx_travel_app/
├── alx_travel_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── listings/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── .env              # ← your env config
├── requirements.txt
```

---

## 🛠️ API Docs (Swagger)

Using **drf-yasg**, auto-generated docs live at:

* `/swagger/` for Swagger UI
* `/redoc` for Redoc

These endpoints are **publicly accessible** with `AllowAny` permissions.

## 🧠 Coming Next

* Auth setup (JWT or session)
* Pagination, filtering
* Docker / K8s deployment
* CI/CD + tests


