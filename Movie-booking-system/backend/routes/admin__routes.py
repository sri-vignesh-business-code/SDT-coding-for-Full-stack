from flask import Blueprint, request, jsonify
from models import db, Movie, Showtime

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/add_movie', methods=['POST'])
def add_movie():
    data = request.json
    movie = Movie(title=data['title'], description=data['description'])
    db.session.add(movie)
    db.session.commit()
    return jsonify({"message": "Movie added"})

@admin_bp.route('/add_showtime', methods=['POST'])
def add_showtime():
    data = request.json
    show = Showtime(movie_id=data['movie_id'], time=data['time'])
    db.session.add(show)
    db.session.commit()
    return jsonify({"message": "Showtime added"})