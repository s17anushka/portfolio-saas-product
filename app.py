import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
CORS(app)

# Session ke liye Secret Key (Zaroori hai login system ke liye)
app.secret_key = os.getenv("SECRET_KEY", "super-secret-portfolio-key-2026")

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/portfolio")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("✅ MongoDB connected successfully!")
except (ConnectionFailure, OperationFailure) as e:
    print(f"❌ MongoDB Connection Error: {e}")

db = client.get_database("portfolio_platform_db")
users_collection = db.users
projects_collection = db.projects

# 1. Landing Page (Signup Builder)
@app.route('/')
def home():
    # Agar pehle se logged in hai, toh uske admin par bhej do
    if 'user' in session:
        return redirect(url_for('admin_panel', username=session['user']))
    return render_template('builder.html')

# 2. Signup Action
@app.route('/create-portfolio', methods=['POST'])
def create_portfolio():
    try:
        data = request.form
        username = data.get('username', '').lower().strip().replace(" ", "")
        password = data.get('password')
        
        if users_collection.find_one({"username": username}):
            return "Username already taken! Please go back and choose another one.", 400

        # Password ko hash (encrypt) karke save karenge
        hashed_password = generate_password_hash(password)

        new_user = {
            "username": username,
            "password": hashed_password,
            "name": data.get('name'),
            "role": data.get('role'),
            "bio": data.get('bio'),
            "github": data.get('github', '#'),
            "linkedin": data.get('linkedin', '#'),
            "email": data.get('email')
        }
        users_collection.insert_one(new_user)
        
        # Naya account bante hi automatically login kar do
        session['user'] = username
        return redirect(url_for('admin_panel', username=username))
    except Exception as e:
        return f"An internal error occurred: {str(e)}", 500

# 3. Login Page & Action
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').lower().strip().replace(" ", "")
        password = request.form.get('password')
        
        user = users_collection.find_one({"username": username})
        
        # Check if user exists aur password match ho raha hai
        if user and check_password_hash(user['password'], password):
            session['user'] = username
            return redirect(url_for('admin_panel', username=username))
        else:
            return "Invalid Username or Password. Please go back and try again.", 401
            
    return render_template('login.html')

# 4. Logout Action
@app.route('/logout')
def logout():
    session.pop('user', None) # Session se user hata do
    return redirect(url_for('login'))

# 5. Dynamic Public Portfolio View
@app.route('/<username>')
def view_portfolio(username):
    try:
        user_data = users_collection.find_one({"username": username.lower()})
        if not user_data:
            return "Portfolio Not Found! Create yours at the homepage.", 404
        return render_template('index.html', user=user_data, username=username.lower())
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# 6. SECURED Admin Page
@app.route('/<username>/admin')
def admin_panel(username):
    # Check if user is logged in aur wahi apna admin khol raha hai
    if 'user' not in session or session['user'] != username.lower():
        return redirect(url_for('login'))
        
    try:
        user_data = users_collection.find_one({"username": username.lower()})
        if not user_data:
            return "User does not exist.", 404
        return render_template('admin.html', username=username.lower())
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# APIs for Projects (Unchanged)
@app.route('/api/projects/<username>', methods=['GET'])
def get_projects(username):
    projects = list(projects_collection.find({"username": username.lower()}, {'_id': 0}))
    return jsonify(projects)

@app.route('/api/projects', methods=['POST'])
def add_project():
    data = request.json
    tech_input = data.get('tech_stack', [])
    tech_stack = [tech.strip() for tech in tech_input.split(',')] if isinstance(tech_input, str) else tech_input
    new_project = {
        "username": data['username'].lower(),
        "title": data['title'],
        "description": data['description'],
        "tech_stack": tech_stack,
        "github_link": data.get('github_link', ''),
        "live_link": data.get('live_link', '')
    }
    projects_collection.insert_one(new_project)
    return jsonify({"message": "Project added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)