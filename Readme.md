<div align="center">

# ✨ Portfolio Builder SaaS

*A sleek, multi-user platform for creators to generate, host, and manage stunning glassmorphism portfolios instantly.*

[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)

</div>

---

## 🎨 The Vision

Built at the intersection of robust backend architecture and premium frontend aesthetics. This platform allows developers and creators to bypass the hassle of coding a portfolio from scratch. By simply filling out an onboarding form, users generate a personalized, live URL featuring a dark-themed, highly responsive UI with fluid animations.

---

## 🚀 Key Features

* 🌍 **Multi-User Architecture:** Instantly generate unique, shareable URLs (e.g., `your-domain.com/username`).
* 🔐 **Secure Authentication:** Built-in login/signup flows with encrypted password hashing.
* 🎛️ **Secret Admin Dashboard:** A protected route for users to effortlessly manage and inject new projects into their live portfolio.
* ⚡ **Real-Time Live Sync:** Projects added via the dashboard reflect instantly on the public view without rebuilding.
* 💎 **Premium UI/UX:** Crafted with Tailwind CSS, featuring glassmorphism elements, ambient background glows, and smooth scroll behaviors.

---

## 🛠️ Technology Stack

| Architecture | Technologies Used |
| :--- | :--- |
| **Backend** | Python, Flask, Flask-CORS, Werkzeug Security |
| **Database** | MongoDB Atlas, PyMongo |
| **Frontend** | HTML5, Tailwind CSS, Vanilla JavaScript |
| **Environment** | Python-dotenv |

---

## 🚦 Getting Started

Follow these steps to set up the development environment locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/s17anushka/portfolio-saas-product.git](https://github.com/s17anushka/portfolio-saas-product.git)
cd portfolio-saas-product

2. Create a Virtual Environment
Isolate your dependencies to keep your global workspace clean.

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory. Add your secure MongoDB connection string and a secret key for session management:

Code snippet
MONGO_URI="mongodb+srv://<username>:<password>@cluster0.xxxx.mongodb.net/?retryWrites=true&w=majority"
SECRET_KEY="your-random-secret-key-here"
5. Launch the Application
Bash
python app.py
Note: The server will start on http://127.0.0.1:5000/.

📱 User Journey
Onboarding: Navigate to the home page (/) to select a unique username and establish a secure password.

Dashboard Access: Post-signup, you are routed to your private admin dashboard (/<username>/admin).

Content Injection: Submit project details (Title, Tech Stack, URLs) via the dashboard form.

Publish: Your work is now live! Copy your shareable link (/<username>) and distribute it to recruiters and peers.

📄 License
MIT License

Copyright (c) 2026 Anushka