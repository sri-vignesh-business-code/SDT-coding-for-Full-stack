import React, { useEffect, useState } from "react";
import API from "../services/api";

function SeatSelection({ showId }) {
  const [seats, setSeats] = useState([]);
  const [selected, setSelected] = useState([]);

  useEffect(() => {
    API.get(`/seats/${showId}`).then(res => setSeats(res.data));
  }, [showId]);

  const toggleSeat = (seat) => {
    if (seat.is_booked) return;

    if (selected.includes(seat.id)) {
      setSelected(selected.filter(id => id !== seat.id));
    } else {
      setSelected([...selected, seat.id]);
    }
  };

  const book = () => {
    API.post("/book", {
      showtime_id: showId,
      seats: selected
    }).then(() => alert("Booked!"));
  };

  return (
    <div>
      <h4>Select Seats</h4>
      {seats.map(seat => (
        <button
          key={seat.id}
          onClick={() => toggleSeat(seat)}
          disabled={seat.is_booked}
          style={{
            background: selected.includes(seat.id) ? "green" : "gray",
            margin: "5px"
          }}
        >
          {seat.seat_number}
        </button>
      ))}
      <br />
      <button onClick={book}>Confirm Booking</button>
    </div>
  );
}

export default SeatSelection;