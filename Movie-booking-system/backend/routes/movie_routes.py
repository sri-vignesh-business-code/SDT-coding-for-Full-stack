from flask import Blueprint, jsonify
from models import Movie, Showtime

movie_bp = Blueprint('movies', __name__)

@movie_bp.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([
        {"id": m.id, "title": m.title, "description": m.description}
        for m in movies
    ])

@movie_bp.route('/showtimes/<int:movie_id>', methods=['GET'])
def get_showtimes(movie_id):
    shows = Showtime.query.filter_by(movie_id=movie_id).all()
    return jsonify([
        {"id": s.id, "time": s.time}
        for s in shows
    ])