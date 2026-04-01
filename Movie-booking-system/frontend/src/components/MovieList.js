import React, { useEffect, useState } from "react";
import API from "../services/api";
import ShowTimes from "./ShowTimes";

function MovieList() {
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);

  useEffect(() => {
    API.get("/movies").then(res => setMovies(res.data));
  }, []);

  return (
    <div>
      <h2>Movies</h2>
      {movies.map(m => (
        <div key={m.id}>
          <h3>{m.title}</h3>
          <button onClick={() => setSelectedMovie(m.id)}>
            View Showtimes
          </button>
        </div>
      ))}

      {selectedMovie && <ShowTimes movieId={selectedMovie} />}
    </div>
  );
}

export default MovieList;