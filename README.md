# 📝 ToDo List Collaboration Project

A modern, fullstack ToDo list application built with **Flask** and **FastAPI**, demonstrating clean separation of frontend and backend responsibilities.

---

## 🎯 Overview

This project is a collaborative effort:

- **Flask** serves as the **UI layer** rendering templates and managing user sessions.
- **FastAPI** is the **API backend**, providing authentication and CRUD endpoints.

This architecture showcases a microfrontend + microbackend pattern, ready for future scaling (e.g., swapping Flask with React or adding a mobile app).

---

##🙌 Contributors

Hacker JOE (Flask Frontend)

Troubleman (FastAPI Backend)

---

## ✨ Features

✅ User Registration & Login  
✅ JWT Authentication  
✅ Create, View, Delete Tasks  
✅ Clean, Modern UI  
✅ Separation of Concerns (Flask purely frontend, FastAPI purely backend)

---

## ⚙️ Technology Stack

- **Frontend:**
  - Flask
  - HTML5 + CSS3
  - JavaScript (Fetch API)

- **Backend:**
  - FastAPI
  - SQLAlchemy
  - Pydantic

- **Database:**
  - SQLite (development)

---

## 🛠️ Project Structure

project-root/
│
├── backend_fastapi/
│ ├── app/
│ │ ├── main.py # FastAPI app entrypoint
│ │ ├── auth.py # Auth routes
│ │ ├── todos.py # Task CRUD routes
│ │ ├── models.py # SQLAlchemy models
│ │ ├── schemas.py # Pydantic schemas
│ │ ├── utils.py # JWT helpers and hashing
│ │ └── database.py # DB engine and session
│ └── requirements.txt
│
├── frontend_flask/
│ ├── app.py # Flask app entrypoint
│ ├── templates/
│ │ ├── login.html
│ │ └── dashboard.html
│ └── static/
│ └── js/
│ └── main.js
└── README.md

yaml
Copy
Edit

---

## 🚀 Running the Application

### 1️⃣ Start FastAPI Backend

From `backend_fastapi/app`:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Make sure your environment has:

nginx
Copy
Edit
fastapi
uvicorn
sqlalchemy
pydantic
python-dotenv
2️⃣ Start Flask Frontend
From frontend_flask:

bash
Copy
Edit
python app.py
Make sure your environment has:

nginx
Copy
Edit
flask
requests
🔑 Authentication Flow
User registers or logs in via FastAPI (/register or /login).

FastAPI returns a JWT access token.

Flask stores this token in the session.

All task API calls (/todos) include the Authorization: Bearer <token> header.

📝 Example .env for FastAPI
ini
Copy
Edit
DATABASE_URL=sqlite:///../shared/database.db
SECRET_KEY=your-secret-key
💡 Recommendations for Production
Switch SQLite to PostgreSQL or MySQL.

Use Docker Compose to run both services.

Enable HTTPS.

Store JWT in HttpOnly cookies instead of JS storage.

Add test coverage (Pytest).



📜 License
MIT License

🎯 Lessons Learned
Cross-origin authentication requires careful handling of CORS and JWT headers.

Microservice-style separation improves maintainability.

Clean API contracts are essential for collaboration.

