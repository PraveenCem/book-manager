import { useState, useEffect } from 'react'
import AddBook from './components/AddBook';
import EditBook from "./components/EditBook";
import DeleteBook from './components/DeleteBook';
import BookReviews from './components/BookReviews';

import "./App.css";


const API_URL = "http://127.0.0.1:8000";

function App() {

  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [editingBook, setEditingBook] = useState(null);

  const fetchBooks = async () => {
    try {
      setLoading(true);

      const response = await fetch(`${API_URL}/books`);

      if (!response.ok) {
        throw new Error("Failed to fetch books");
      }

      const data = await response.json();

      setBooks(data.books);
      setError("");
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  useEffect(() => {
    document.title = "Book Manager 📚";
  }, []);

  if (loading) {
    return <h2>Loading Books...</h2>
  }

  if (error) {
    return <h2>{error}</h2>
  }

  return (
    <div>
      <h1>Book Manager</h1>
      <AddBook onBookAdd={fetchBooks} />
      {books.map((book) => (
        <div className="book" key={book._id}>
          {editingBook?._id === book._id ? (
            <EditBook
              book={book}
              onBookUpdated={() => {
                setEditingBook(null);
                fetchBooks();
              }}
              onCancel={() => setEditingBook(null)}
            />
          ) : (
            <>
              <h2>{book.title}</h2>
              <p>Author: {book.author}</p>
              <p>Year: {book.year}</p>
              <p>Genres: {book.genres.join(", ")}</p>

              <button onClick={() => setEditingBook(book)}>
                Edit
              </button>
              <DeleteBook bookId={book._id} onBookDeleeted={fetchBooks} />
              <BookReviews bookId={book._id} />
            </>
          )}
        </div>
      ))}
    </div>
  );
}

export default App
