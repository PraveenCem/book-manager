import { useState,useEffect } from "react";

const API_URL = "http://127.0.0.1:8000";


function ReviewList({bookId,refreshKey}){
    const [reviews,setReviews] = useState("");
    const [loading,setLoading] = useState(true);
    const [error,setError] = useState("");

    const fetchReviews = async () =>{
        try{
            setLoading(true);
            const response = await fetch(`${API_URL}/books/${bookId}/reviews`);
            if(!response.ok){
                throw new Error("Failed to fetch reviews.");
            }

            const data = await response.json();
            setReviews(data);
            setError("");
        }catch(error){
            setError(error.message);
        }finally{
            setLoading(false);
        }
    };

    useEffect(()=>{
        fetchReviews();
    },[bookId,refreshKey]);

    if(loading){
        return <p>Loading reviews..</p>;
    }
    
    if(error){
        return <p>{error}</p>;
    }

    if(reviews.length === 0){
        return <p>No reviews yet.</p>;
    }

    return(
        <div>
            <h3>Reviews</h3>
            {reviews.map((review,index)=>(
                <div className="review" key={index}>
                    <strong>{review.user}</strong>
                    <p>Rating: {review.rating}</p>
                    <p>{review.comment}</p>
                </div>  
            ))}
        </div>
    );
}

export default ReviewList;