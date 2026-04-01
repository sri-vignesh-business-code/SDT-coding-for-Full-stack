import React, { useEffect, useState } from "react";
import API from "../services/api";
import SeatSelection from "./SeatSelection";

function ShowTimes({ movieId }) {
  const [shows, setShows] = useState([]);
  const [selectedShow, setSelectedShow] = useState(null);

  useEffect(() => {
    API.get(`/showtimes/${movieId}`)
      .then(res => setShows(res.data));
  }, [movieId]);

  return (
    <div>
      <h3>Showtimes</h3>
      {shows.map(s => (
        <button key={s.id} onClick={() => setSelectedShow(s.id)}>
          {s.time}
        </button>
      ))}

      {selectedShow && <SeatSelection showId={selectedShow} />}
    </div>
  );
}

export default ShowTimes;