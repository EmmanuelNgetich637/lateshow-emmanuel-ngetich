# lateshow-emmanuel-ngetich


A Flask RESTful API for managing TV show guest appearances. Built using Flask, SQLAlchemy, Flask-Migrate, and SQLite.

## Project Structure
lateshow/
│
├── app/
│ ├── init.py 
│ ├── models.py 
│ ├── routes.py 
├── migrations/
├── seed.py 
├── guests.csv 
├── episodes.csv 
├── appearances.csv 
├── config.py
├── run.py 
└── README.md 


---

## 🛠️ Tech Stack

- **Python 3.12**
- **Flask**
- **Flask-SQLAlchemy**
- **Flask-Migrate**
- **SQLite3**
- **Alembic**

---

## 🚀 Setup Instructions

1. **Clone the repo**  
```bash
git clone https://github.com/EmmanuelNgetich637/lateshow-api.git
cd lateshow-api

API Endpoints
GET /episodes
Returns a list of all episodes (with basic info).

GET /guests/<int:id>
Returns a specific guest including their appearances.

POST /appearances
Adds a new guest appearance.

DELETE /appearances/<int:id>
Deletes an appearance by ID.

Error Handling
404 Not Found if guest or appearance does not exist.

400 Bad Request for invalid rating or missing data.

Author
Emmanuel Ngetich
