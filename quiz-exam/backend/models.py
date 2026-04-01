from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

# ---------------- USER MODEL ---------------- #

def create_user(username, password, role="user"):
    hashed_password = generate_password_hash(password)
    
    user = {
        "username": username,
        "password": hashed_password,
        "role": role  # "admin" or "user"
    }
    
    result = db.users.insert_one(user)
    return str(result.inserted_id)


def find_user_by_username(username):
    return db.users.find_one({"username": username})


def verify_user(username, password):
    user = find_user_by_username(username)
    
    if user and check_password_hash(user["password"], password):
        user["_id"] = str(user["_id"])
        return user
    return None


# ---------------- QUIZ MODEL ---------------- #

def create_quiz(title, questions):
    quiz = {
        "title": title,
        "questions": questions
    }
    result = db.quizzes.insert_one(quiz)
    return str(result.inserted_id)


def get_all_quizzes():
    quizzes = list(db.quizzes.find())
    for q in quizzes:
        q["_id"] = str(q["_id"])
    return quizzes


def get_quiz_by_id(quiz_id):
    quiz = db.quizzes.find_one({"_id": ObjectId(quiz_id)})
    if quiz:
        quiz["_id"] = str(quiz["_id"])
    return quiz


# ---------------- RESULT MODEL ---------------- #

def save_result(user, quiz_id, score, total):
    result = {
        "user": user,
        "quiz_id": quiz_id,
        "score": score,
        "total": total
    }
    db.results.insert_one(result)


def get_leaderboard():
    results = list(db.results.find().sort("score", -1))
    for r in results:
        r["_id"] = str(r["_id"])
    return results