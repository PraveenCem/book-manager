import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";


function DeleteBook({ bookId, onBookDeleeted }) {

    const [error, setError] = useState("");

    const handleDelete = async () => {
        try {
            const response = await fetch(`${API_URL}/books/${bookId}`, {
                method: "DELETE",
            });
            if (!response.ok) {
                throw new Error("Failed to delete book.");
            }

            setError("");
            onBookDeleeted();
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <div>
            <button onClick={handleDelete}>
                Delete
            </button>
            {error && <p>{error}</p>}
        </div>
    );

}

export default DeleteBook;