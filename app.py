from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

# ------------------ Database setup ------------------ #
def init_db():
    conn = sqlite3.connect("restaurant.db")
    c = conn.cursor()
    # Users table
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 password TEXT)""")
    # Orders table
    c.execute("""CREATE TABLE IF NOT EXISTS orders (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT,
                 item TEXT,
                 quantity INTEGER)""")
    # Contact messages table
    c.execute("""CREATE TABLE IF NOT EXISTS messages (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 email TEXT,
                 message TEXT)""")
    conn.commit()
    conn.close()

init_db()

# Make session available in all templates
@app.context_processor
def inject_session():
    return dict(session=session)

# ------------------ Routes ------------------ #

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Menu page (newly added to fix BuildError)
@app.route("/menu")
def menu():
    return render_template("menu.html")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = generate_password_hash(request.form["password"])
        try:
            conn = sqlite3.connect("restaurant.db")
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already exists.", "danger")
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        conn = sqlite3.connect("restaurant.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        conn.close()
        if user and check_password_hash(user[2], password):
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("index"))

# Contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        message = request.form["message"].strip()
        conn = sqlite3.connect("restaurant.db")
        c = conn.cursor()
        c.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()
        flash("Message sent successfully!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

# Order page
@app.route("/order", methods=["GET", "POST"])
def order():
    if "username" not in session:
        flash("Please login to place an order", "warning")
        return redirect(url_for("login"))
    if request.method == "POST":
        item = request.form["item"].strip()
        quantity = int(request.form["quantity"])
        conn = sqlite3.connect("restaurant.db")
        c = conn.cursor()
        c.execute("INSERT INTO orders (username, item, quantity) VALUES (?, ?, ?)", (session["username"], item, quantity))
        conn.commit()
        conn.close()
        flash("Order placed successfully!", "success")
    return render_template("order.html")

# Payment page
@app.route("/payment")
def payment():
    return render_template("payment.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Admin panel
@app.route("/admin")
def admin():
    conn = sqlite3.connect("restaurant.db")
    c = conn.cursor()
    c.execute("SELECT * FROM orders")
    orders = c.fetchall()
    c.execute("SELECT * FROM messages")
    messages = c.fetchall()
    conn.close()
    return render_template("admin.html", orders=orders, messages=messages)

# ------------------ Run App ------------------ #
if __name__ == "__main__":
    app.run(debug=True)
