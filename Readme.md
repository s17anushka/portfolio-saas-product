# ✨ Portfolio Builder SaaS

> A modern multi-user SaaS platform that enables developers, designers, and creators to generate beautiful portfolio websites instantly — without writing frontend code.

<div align="center">

### 🚀 Build • Publish • Share

Generate stunning glassmorphism-powered portfolios with your own personalized URL.

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge\&logo=mongodb\&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge\&logo=tailwind-css\&logoColor=white)

</div>

---

# 🌟 Overview

Portfolio Builder SaaS eliminates the complexity of creating and maintaining a personal portfolio website.

Instead of designing pages manually, users simply sign up, fill in their details, and instantly receive a fully hosted portfolio with a unique public URL.

Built using Flask, MongoDB Atlas, and Tailwind CSS, the platform provides a seamless experience for both portfolio creation and content management.

---

# ✨ Features

### 🌐 Multi-User Portfolio Hosting

Each user gets a dedicated portfolio URL:

```text
your-domain.com/username
```

### 🔐 Secure Authentication

* User Signup & Login
* Password Hashing using Werkzeug Security
* Protected User Sessions

### 🎛️ Personal Admin Dashboard

Every user receives a private dashboard to:

* Add Projects
* Manage Portfolio Content
* Update Portfolio Information
* Publish Changes Instantly

### ⚡ Real-Time Updates

New projects added through the dashboard automatically appear on the live portfolio without requiring any rebuild or deployment.

### 🎨 Premium UI Experience

* Glassmorphism Design
* Dark Theme
* Responsive Layout
* Smooth Animations
* Ambient Background Effects
* Mobile Friendly

---

# 🏗️ System Architecture

```text
┌─────────────────────────────┐
│          Users              │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Flask Backend         │
│ Authentication & Routing    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      MongoDB Atlas          │
│ User Data & Projects        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Dynamic Portfolio Rendering │
└─────────────────────────────┘
```

---

# 🛠️ Tech Stack

| Layer       | Technologies                    |
| ----------- | ------------------------------- |
| Backend     | Python, Flask, Flask-CORS       |
| Security    | Werkzeug Password Hashing       |
| Database    | MongoDB Atlas, PyMongo          |
| Frontend    | HTML5, Tailwind CSS, JavaScript |
| Environment | Python-dotenv                   |

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/s17anushka/portfolio-saas-product.git

cd portfolio-saas-product
```

---

## 2️⃣ Create Virtual Environment

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/

SECRET_KEY=your-secret-key
```

---

## 5️⃣ Run the Application

```bash
python app.py
```

Application will be available at:

```text
http://127.0.0.1:5000
```

---

# 📱 User Workflow

### Step 1: Sign Up

Create a unique username and password.

### Step 2: Access Dashboard

Navigate to:

```text
/username/admin
```

### Step 3: Add Projects

Submit:

* Project Title
* Description
* Technologies Used
* GitHub Link
* Live Demo Link

### Step 4: Publish

Your portfolio becomes instantly available at:

```text
/username
```

Share it with recruiters, clients, and peers.

---

# 🔒 Security Features

* Password Hashing
* Session Protection
* Environment Variable Management
* Protected Admin Routes
* MongoDB Atlas Secure Storage

---

# 🎯 Future Enhancements

* Resume Upload Support
* Multiple Portfolio Themes
* Drag & Drop Project Management
* Custom Domains
* Analytics Dashboard
* Portfolio SEO Optimization
* AI Portfolio Generator

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

MIT License

Copyright © 2026 Anushka Singh

---

<div align="center">

### ⭐ If you like this project, consider giving it a star!

Built with ❤️ using Flask, MongoDB & Tailwind CSS

</div>
