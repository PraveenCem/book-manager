# 📚 Book Manager PoC

A minimal, production-oriented proof of concept built to learn and demonstrate **MongoDB operations** using a **Python FastAPI backend** and a **React frontend**.

The project focuses on understanding MongoDB querying, filtering, indexing, aggregation, embedded documents, and REST API design through a practical Book Manager application.

---

## 🚀 Tech Stack

### 🗄️ Database
- **MongoDB**
- MongoDB Community Server
- Embedded documents for book reviews
- MongoDB indexes
- Aggregation pipelines

### ⚙️ Backend
- **Python**
- **FastAPI**
- **Pydantic**
- **Motor** — Async MongoDB driver
- **PyMongo**
- Repository pattern
- REST APIs

### 🎨 Frontend
- **React**
- **Vite**
- JavaScript
- CSS
- React Hooks (`useState`, `useEffect`)

---

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │   React + Vite  │
                    │    Frontend     │
                    └────────┬────────┘
                             │
                         HTTP / REST
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    │     Routes      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Repository    │
                    │     Layer       │
                    └────────┬────────┘
                             │
                          Motor
                             │
                             ▼
                    ┌─────────────────┐
                    │     MongoDB     │
                    │    Database     │
                    └─────────────────┘


book-manager/
│
├── backend/
│   ├── .env
│   ├── .gitignore
│   │
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   │
│   │   ├── models/
│   │   │   ├── book.py
│   │   │   └── book_repo.py
│   │   │
│   │   └── routes/
│   │       └── book.py
│   │
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AddBook.jsx
│   │   │   ├── EditBook.jsx
│   │   │   ├── DeleteBook.jsx
│   │   │   ├── BookReviews.jsx
│   │   │   ├── ReviewList.jsx
│   │   │   └── AddReview.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
└── README.md
