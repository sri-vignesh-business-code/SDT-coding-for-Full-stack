from flask import Blueprint, request, jsonify
import jwt
import datetime
from models import create_user, verify_user
from app import db

SECRET_KEY = "your_secret_key"

auth_routes = Blueprint("auth_routes", __name__)

# ---------------- REGISTER ---------------- #

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.json

    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "user")

    # Check if user exists
    existing = db.users.find_one({"username": username})
    if existing:
        return jsonify({"message": "User already exists"}), 400

    user_id = create_user(username, password, role)

    return jsonify({
        "message": "User registered",
        "user_id": user_id
    })


# ---------------- LOGIN ---------------- #

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    user = verify_user(username, password)

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode({
        "user_id": user["_id"],
        "username": user["username"],
        "role": user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({
        "token": token,
        "user": {
            "username": user["username"],
            "role": user["role"]
        }
    })


# ---------------- PROTECTED ROUTE EXAMPLE ---------------- #

@auth_routes.route("/profile", methods=["GET"])
def profile():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"message": "Token missing"}), 403

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({
            "user_id": data["user_id"],
            "username": data["username"],
            "role": data["role"]
        })
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 401
    except:
        return jsonify({"message": "Invalid token"}), 401