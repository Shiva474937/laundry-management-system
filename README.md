# Laundry Order Management System

## 📌 Features
- Create Order with total bill calculation
- Update Order Status (RECEIVED → PROCESSING → READY → DELIVERED)
- View all Orders
- Dashboard (Total Orders & Revenue)

##  Setup Instructions

1. Install Python (3.13 recommended)
2. Install Flask:
   pip install flask
3. Run the application:
   python app.py

4. Server will start at:
   http://127.0.0.1:5000

---

##  API Endpoints

### 1. Create Order
POST /create

### 2. Get All Orders
GET /orders

### 3. Update Order Status
PUT /status/<id>

### 4. Dashboard
GET /dashboard

---

##  Testing
- Tested using Thunder Client (VS Code)

---

##  AI Usage Report

- Used ChatGPT to generate Flask API
- Fixed Python & Flask errors
- Tested APIs using Thunder Client

---

##  Limitations
- No database (data resets on restart)
- No frontend UI
- No authentication
- Data resets when server restarts (in-memory storage)

---

##  Tech Stack
- Python
- Flask
