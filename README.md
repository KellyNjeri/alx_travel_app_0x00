# 🛫 ALX Travel App 0x00

A Django backend project for managing travel listings, bookings, and reviews. This project demonstrates **database modeling**, **API serialization**, and **database seeding** with Django and Django REST Framework (DRF).  

---

## 📌 Features
- Define relational models (`Listing`, `Booking`, `Review`).
- Use DRF serializers to transform model data into JSON.
- Seed the database with sample data using a custom management command.
- Provide clean and consistent test data for development.

---

## 🏗️ Project Structure
alx_travel_app_0x00/
│── README.md
│── manage.py
│── db.sqlite3
│
├── alx_travel_app/ # Main project settings
│ └── settings.py, urls.py...
│
├── listings/ # App for listings, bookings, reviews
│ ├── models.py # Database models
│ ├── serializers.py # DRF serializers
│ ├── views.py # API views (if added)
│ ├── urls.py # App routes (if added)
│ └── management/
│ └── commands/
│ └── seed.py # Seeder command


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/alx_travel_app_0x00.git
   cd alx_travel_app_0x00
   Create a virtual environment

python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py makemigrations
python manage.py migrate


Run the development server

python manage.py runserver

🌱 Database Seeding

To populate the database with sample listings:

python manage.py seed


This will create a few sample travel listings 

## 🔍 Testing in Django Shell
python manage.py shell
>>> from listings.models import Listing
>>> Listing.objects.all()

## 🛠️ Tools & Libraries

Django – backend framework

Django REST Framework (DRF) – serializers and API

SQLite – default database (can switch to PostgreSQL)

Python 3.x

## 📄 License

This project is for educational purposes under the ALX Software Engineering/Data Science Program.