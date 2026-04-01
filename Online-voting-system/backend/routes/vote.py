from flask import Blueprint, request, jsonify
from models import db, Vote
from flask_jwt_extended import jwt_required, get_jwt_identity

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/cast', methods=['POST'])
@jwt_required()
def cast_vote():
    user_id = get_jwt_identity()
    data = request.json

    existing = Vote.query.filter_by(user_id=user_id, election_id=data['election_id']).first()
    if existing:
        return jsonify({"msg": "Already voted"}), 400

    vote = Vote(user_id=user_id,
                election_id=data['election_id'],
                candidate_id=data['candidate_id'])

    db.session.add(vote)
    db.session.commit()
    return jsonify({"msg": "Vote casted"})