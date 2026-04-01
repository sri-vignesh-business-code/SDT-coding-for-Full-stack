from flask import Blueprint, request, jsonify
from app import db

result_routes = Blueprint("result_routes", __name__)

# Submit quiz
@result_routes.route("/submit", methods=["POST"])
def submit_quiz():
    data = request.json

    score = 0
    for q in data["questions"]:
        if q["selected"] == q["answer"]:
            score += 1

    result = {
        "user": data["user"],
        "quiz_id": data["quiz_id"],
        "score": score,
        "total": len(data["questions"])
    }

    db.results.insert_one(result)
    return jsonify(result)

# Leaderboard
@result_routes.route("/leaderboard", methods=["GET"])
def leaderboard():
    results = list(db.results.find().sort("score", -1))
    for r in results:
        r["_id"] = str(r["_id"])
    return jsonify(results)