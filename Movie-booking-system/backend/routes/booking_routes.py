from flask import Blueprint, request, jsonify
from models import db, Seat, Booking

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/seats/<int:showtime_id>', methods=['GET'])
def get_seats(showtime_id):
    seats = Seat.query.filter_by(showtime_id=showtime_id).all()
    return jsonify([
        {"id": s.id, "seat_number": s.seat_number, "is_booked": s.is_booked}
        for s in seats
    ])

@booking_bp.route('/book', methods=['POST'])
def book_seats():
    data = request.json
    booking = Booking(
        showtime_id=data['showtime_id'],
        seats=",".join(data['seats'])
    )

    for seat_id in data['seats']:
        seat = Seat.query.get(seat_id)
        seat.is_booked = True

    db.session.add(booking)
    db.session.commit()

    return jsonify({"message": "Booking successful"})