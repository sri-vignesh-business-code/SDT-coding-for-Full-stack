from flask import Blueprint, request, jsonify
from app import db
from bson.objectid import ObjectId

quiz_routes = Blueprint("quiz_routes", __name__)

# Create Quiz (Admin)
@quiz_routes.route("/create", methods=["POST"])
def create_quiz():
    data = request.json
    db.quizzes.insert_one(data)
    return jsonify({"message": "Quiz created"})

# Get all quizzes
@quiz_routes.route("/", methods=["GET"])
def get_quizzes():
    quizzes = list(db.quizzes.find())
    for q in quizzes:
        q["_id"] = str(q["_id"])
    return jsonify(quizzes)

# Get single quiz
@quiz_routes.route("/<id>", methods=["GET"])
def get_quiz(id):
    quiz = db.quizzes.find_one({"_id": ObjectId(id)})
    quiz["_id"] = str(quiz["_id"])
    return jsonify(quiz)