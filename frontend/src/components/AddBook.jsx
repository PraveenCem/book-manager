import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";

function AddBook({onBookAdd}) {

    const [title,setTitle] = useState("");
    const [author,setAuthor] = useState("");
    const [year,setYear] = useState("");
    const [genres,setGenres] = useState("");

    const handleSubmit = async(event) => {
        event.preventDefault();

        const response = await fetch(`${API_URL}/books`,{
            method: "POST",
            headers:{
                "Content-Type": "application/json",
            },
            body:JSON.stringify({
                title,
                author,
                year:Number(year),
                genres: genres.split(",").map((genre)=>genre.trim()),
            }),
        });

        if(!response.ok){
            throw new Error("Failed to add book");
        }

        setTitle("");
        setAuthor("");
        setYear("");
        setGenres("");

        onBookAdd();
    };

    return(
        <div>
            <h2>Add Book</h2>
            <form onSubmit={handleSubmit}>
                <input type="text"
                    placeholder="Title"
                    value={title}
                    onChange={(event)=>setTitle(event.target.value)}
                />
                <input type="text"
                    placeholder="Author"
                    value={author}
                    onChange={(event)=>setAuthor(event.target.value)}
                />
                <input type="number"
                    placeholder="Year"
                    value={year}
                    onChange={(event)=>setYear(event.target.value)}
                />
                <input type="text"
                    placeholder="Genres(comma seperated)"
                    value={genres}
                    onChange={(event)=>setGenres(event.target.value)}
                />   
                <button type="submit">Add Book</button> 
            </form>               
        </div>
    );
}

export default AddBook;