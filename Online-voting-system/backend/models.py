from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)

class Election(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    election_id = db.Column(db.Integer, db.ForeignKey('election.id'))

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    election_id = db.Column(db.Integer)
    candidate_id = db.Column(db.Integer)