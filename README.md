# Smart Vehicle Maintenance Intelligence System (SVMIS) 🚗💨

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-3.0%2B-lightgrey)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/database-PostgreSQL-green)](https://www.postgresql.org/)

SVMIS is a premium, production-ready intelligent vehicle maintenance ecosystem. It doesn't just track service history; it uses real-time odometer data to predict upcoming maintenance needs, calculates a proprietary "Vehicle Health Score," and provides a high-fidelity glassmorphism dashboard for expense analytics.

---

## 🌟 Key Features

### 🔐 Advanced Authentication
- Secure User Registration and Multi-Session Login.
- Password hashing with **Bcrypt** for enterprise-grade security.
- Profile management and personalized user experience.

### 📊 Intelligent Dashboard
- **Glassmorphism UI**: A sleek, modern dark-themed interface with subtle micro-animations.
- **Cost Analytics**: Interactive charts (Chart.js) showing monthly spending trends and category breakdowns.
- **Visual Health Indicators**: Progress bars and status badges (Urgent/Soon/Good) based on service proximity.

### 🧠 Smart Prediction Engine
- **Automated Service Forecasting**: Predicts intervals for Oil changes (3k km), Brake checks (6k km), Tire rotations (10k km), and more.
- **Health Score Calculation**: A weighted algorithm that assesses overall vehicle reliability based on maintenance compliance.

### 🛠️ Maintenance & Expense Tracking
- **Detailed History**: A chronological timeline of every service performed.
- **Expense Integration**: Every maintenance record automatically syncs with the cost analytics engine.
- **Customizable Records**: Logs date, odometer, cost, service type, and detailed technician notes.

---

## 🏗️ System Architecture

### 📁 Directory Structure
```
vehicle-maintenance-system/
├── app.py                  # Application Entry Point & Factory
├── config.py               # Environment Configuration
├── models/
│   └── models.py           # SQLAlchemy Data Models & Logic
├── routes/                 # Modular Blueprints
│   ├── auth_routes.py      # Identity & Access Management
│   ├── vehicle_routes.py   # Fleet Inventory Control
│   ├── maintenance_routes.py # Service Lifecycle
│   ├── analytics_routes.py # Business Intelligence
│   └── notification_routes.py # Event Logs
├── services/               # Core Logic & Integration
│   ├── maintenance_predictor.py # AI Prediction Logic
│   ├── analytics_service.py # Data Aggregation
│   └── notification_service.py # Messaging & Email
└── static/                 # Frontend Assets
    ├── css/style.css       # Custom Design System
    └── js/main.js          # Client-side Logic
```

---

## 🚀 Installation Guide

### Prerequisites
- Python 3.8+
- PostgreSQL (or a Neon.tech connection string)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/harshith1432/Smart-Vehicle-Maintenance.git
   cd vehicle-maintenance-system
   ```

2. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your_secure_random_key
   DATABASE_URL=postgresql://user:password@hostname/dbname?sslmode=require
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_EMAIL=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize & Run**
   ```bash
   python app.py
   ```
   🚀 Access the portal at `http://127.0.0.1:5000`

---

## 🛡️ Security & Performance
- **Flask-Login**: Robust session management and route protection.
- **CSRF Protection**: Native Flask security patterns.
- **Neon Postgres**: Serverless PostgreSQL for auto-scaling and high availability.
- **Asset Optimization**: Minimized static loads and efficient ORM queries.

---

## 👨‍💻 Contributing
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Dedicated to high-performance vehicle care. Crafted with 💡 by Antigravity.**

