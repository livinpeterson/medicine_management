Medical Store Management Project

Overview:
  This project aims to provide a comprehensive solution for managing a medical store's inventory, sales, and customer information using Django framework with REST API.

Features:
    Inventory Management: Keep track of medicines, their quantities, and expiration dates.
Sales Management: Record sales transactions and generate invoices for customers.
Customer Management: Maintain a database of customer information for easy reference.
User Authentication: Secure access to the system with user authentication and authorization.

Technologies Used:
  Django: Python web framework for backend development.
  Django REST Framework: Toolkit for building Web APIs with Django.
  MySQL: Relational database management system for storing data.
  HTML/CSS/JavaScript: Frontend development for user interface.

Setup Instructions:

  Clone the Repository:
    git clone https://github.com/livinpeterson/medical-store-management.git

  Install Dependencies:
    pip install -r requirements.txt

  Database Setup:
    Create a MysQL database for the project.
    Update database settings in settings.py file.

  Run Migrations:
    python manage.py makemigrations
    python manage.py migrate

  Start the Server:
    python manage.py runserver

Access the Application:
  Open your web browser and navigate to http://localhost:8000.
  API Endpoints
  GET /api/medicines/: Retrieve all medicines.
  POST /api/medicines/: Create a new medicine.
  GET /api/medicines/{id}/: Retrieve details of a specific medicine.
  PUT /api/medicines/{id}/: Update details of a specific medicine.
  DELETE /api/medicines/{id}/: Delete a specific medicine.
