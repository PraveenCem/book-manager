import { useState } from "react";
import ReviewList from "./ReviewList";
import AddReview from "./AddReview";


function BookReviews({bookId}){

    const [refreshKey,setRefreshKey] = useState(0);
    const handleReviewAdded=()=>{
        setRefreshKey((value) => value + 1);
    }

    return(
        <div>
            <ReviewList bookId={bookId} refreshKey={refreshKey} />
            <AddReview bookId={bookId} onReviewAdded={handleReviewAdded} />
        </div>
    );
}

export default BookReviews;