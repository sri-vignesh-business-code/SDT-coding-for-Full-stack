from flask import Blueprint, jsonify
from models import db, Vote, Candidate
from sqlalchemy import func

results_bp = Blueprint('results', __name__)

@results_bp.route('/<int:election_id>')
def get_results(election_id):
    results = db.session.query(
        Candidate.name,
        func.count(Vote.id)
    ).join(Vote, Candidate.id == Vote.candidate_id)\
     .filter(Vote.election_id == election_id)\
     .group_by(Candidate.name).all()

    return jsonify([{"candidate": r[0], "votes": r[1]} for r in results])