# User Registration Application

A Django-based User registration application to manage tasks across categories with features like priority, image uploads, and theme toggling.

**Last Updated:** 05:55 PM IST, Saturday, June 07, 2025

## Prerequisites
- Python 3.8+
- pip
- Virtualenv (optional but recommended)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd todo-list-app
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```
   Or install Django manually:
   ```bash
   pip install django==4.2
   ```

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```
   Type `yes` if prompted.

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000`.

## Notes
- Ensure an active internet connection for package installation.
- Use `deactivate` to exit the virtual environment.