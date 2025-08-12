🍽 Restaurant Management System
A simple Flask + SQLite web application for managing a restaurant’s orders, menu, payments, and customer interactions.
The project keeps all backend logic and database setup in a single app.py file while using clean and modular HTML templates with a shared base.html.

🚀 Features
User Authentication

Register & Login pages

Session-based login management

Menu & Orders

Browse the restaurant menu

Place food orders online

Payments

Mock payment page for order checkout

Contact Page

Send messages or inquiries

Admin Dashboard

View and manage customer orders

Database

SQLite database stored and managed directly in app.py







📂 Project Structure

restaurant_system/
│── app.py                 # Main Flask application (backend + database)
│── templates/             # HTML templates
│   │── base.html           # Main base template
│   │── index.html          # Home page
│   │── menu.html           # Menu page
│   │── order.html          # Order page
│   │── payment.html        # Payment page
│   │── about.html          # About Us page
│   │── contact.html        # Contact page
│   │── login.html          # User login page
│   │── register.html       # User registration page
│   │── admin.html          # Admin dashboard
│── static/                 # CSS, JS, and images
 style.css :- in static folder 



🛠 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/restaurant_system.git
cd restaurant_system

2️⃣ Create a virtual environment & activate it

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


3️⃣ Install dependencies

pip install flask

4️⃣ Run the application

python app.py

The app will be available at http://127.0.0.1:5000

📸 Screenshots
Home Page	Menu Page

📌 Technologies Used
Python 3

Flask (Web framework)

SQLite (Database)

HTML, CSS, JavaScript (Frontend)

🔑 Admin Access
The admin dashboard can be accessed via:


http://127.0.0.1:5000/admin

(Default admin credentials are set inside app.py.)


📜 License
This project is licensed under the MIT License.




 
