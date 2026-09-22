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

## Project Structure


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



📚 Book Manager — Features Added
📖 Book Management
➕ Add new books
👀 View/list all books
🔍 View a single book
✏️ Edit/update books
🗑️ Delete books
🔎 Search & Filtering
🔍 Search by title, author, and genre
👤 Case-insensitive author search
📅 Filter by minimum year
📅 Filter by maximum year
🎭 Filter by multiple genres
🚫 Exclude a specific publication year
🚫 Exclude specific genres
🔀 Combine multiple filters
↕️ Sorting
⬆️ Sort ascending
⬇️ Sort descending
🔤 Dynamic sorting by selected field
📄 Pagination
📑 Page-based pagination
🔢 Configurable page size
📊 Total record count
📚 Total page count
⏭️ Skip/limit implementation
🗄️ MongoDB Features
🆔 MongoDB ObjectId handling
🔎 Regex queries
🎯 $in
🚫 $nin
⚖️ $ne
🔀 $or
📊 Aggregation pipelines
⚡ MongoDB indexes
🔬 Query performance using explain()
📈 Genre statistics
📊 Book statistics
⭐ Reviews
⭐ Add reviews to books
👀 View reviews
⭐ 1–5 rating validation
💬 Review comments
👤 Review user information
🗂️ Embedded reviews inside book documents
🔗 Reviews remain associated with their respective books
🛡️ Validation & Error Handling
✅ Pydantic request validation
🆔 Invalid ObjectId validation
❌ Book-not-found handling
❌ Review-not-found handling
⚠️ API error handling
🔢 Review rating validation (1–5)
⚛️ React Frontend
⚛️ React + Vite
🧩 Component-based architecture
➕ AddBook
✏️ EditBook
🗑️ DeleteBook
⭐ BookReviews
👀 ReviewList
➕ AddReview
🔄 API-driven UI updates
🎨 Custom CSS styling
📱 Basic responsive styling
🏷️ Custom browser tab title


