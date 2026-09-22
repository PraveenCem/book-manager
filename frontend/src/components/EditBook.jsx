import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";

function EditBook({ book, onBookUpdated, onCancel }) {
  const [title, setTitle] = useState(book.title);
  const [author, setAuthor] = useState(book.author);
  const [year, setYear] = useState(book.year);
  const [genres, setGenres] = useState(book.genres.join(", "));

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch(`${API_URL}/books/${book._id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title,
        author,
        year: Number(year),
        genres: genres.split(",").map((genre) => genre.trim()),
      }),
    });

    if (!response.ok) {
      throw new Error("Failed to update book");
    }

    onBookUpdated();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
      />

      <input
        type="text"
        value={author}
        onChange={(event) => setAuthor(event.target.value)}
      />

      <input
        type="number"
        value={year}
        onChange={(event) => setYear(event.target.value)}
      />

      <input
        type="text"
        value={genres}
        onChange={(event) => setGenres(event.target.value)}
      />

      <button type="submit">Save</button>

      <button type="button" onClick={onCancel}>
        Cancel
      </button>
    </form>
  );
}

export default EditBook;