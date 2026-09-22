import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";

function AddReview({bookId,onReviewAdded}){
    
    const [user,setUser] = useState("");
    const [rating,setRating] = useState("");
    const [comment,setComment] = useState("");
    const [error,setError] = useState("");

    const handleSubmit = async (event) =>{
        
        event.preventDefault();

        try{
            const response = await fetch(`${API_URL}/books/${bookId}/reviews`,
                {
                    method:"POST",
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body:JSON.stringify({
                        user,
                        rating:Number(rating),
                        comment,
                    }),
                }
            );

            if(!response.ok){
                throw new Error("Failed to add review.");
            }

            setUser("");
            setRating("");
            setComment("");
            setError("");

            onReviewAdded();

        }catch(error){
            setError(error.message);
        }
    };

    return(

        <div>
            <h3>Add Review</h3>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Your name" value={user} onChange={(event)=>setUser(event.target.value)} />
                <input type="text" placeholder="Rating(1-5)" value={rating} onChange={(event)=>setRating(event.target.value)} />
                <input type="text" placeholder="Your comment" value={comment} onChange={(event)=>setComment(event.target.value)} />
                <button type="submit">
                    Add Review
                </button>
            </form>
            {error && <p>{error}</p>}
        </div>
    );
}

export default AddReview;