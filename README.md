# 🧘‍♀️ Amokh Veda – Ayurvedic Learning Platform

A full-stack Django web application focused on spreading the wisdom of Ayurveda through classes, expert consultations, and events.

## 🌿 Features

- 🏠 Beautiful homepage with background images and animations
- 📖 Informative About page
- 🧑‍⚕️ Expert listing with images and specializations
- 📅 Classes and events section
- 📬 Contact form
- 🎨 FontAwesome icons and Bootstrap UI
- 📁 Media and static file support (image uploads, CSS, etc.)

## 🔧 Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript
- **Backend**: Python, Django
- **Database**: SQLite
- **Hosting**: PythonAnywhere
- **Version Control**: Git + GitHub

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Ardra-KP/amokhveda-django.git
cd amokhveda-django

# Create virtual environment
python -m venv env
env\Scripts\activate   # On Windows

# Install requirements
pip install -r requirements.txt

# Run migrations and start server
python manage.py migrate
python manage.py runserver
