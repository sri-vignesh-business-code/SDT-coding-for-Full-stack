from flask import Blueprint, request, jsonify
from models import db, Election, Candidate

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/create-election', methods=['POST'])
def create_election():
    data = request.json
    election = Election(title=data['title'])
    db.session.add(election)
    db.session.commit()
    return jsonify({"msg": "Election created"})

@admin_bp.route('/add-candidate', methods=['POST'])
def add_candidate():
    data = request.json
    candidate = Candidate(name=data['name'], election_id=data['election_id'])
    db.session.add(candidate)
    db.session.commit()
    return jsonify({"msg": "Candidate added"})