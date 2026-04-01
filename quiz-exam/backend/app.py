from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

app = Flask(__name__)
CORS(app)

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Import routes
from routes.quiz import quiz_routes
from routes.result import result_routes

app.register_blueprint(quiz_routes, url_prefix="/quiz")
app.register_blueprint(result_routes, url_prefix="/result")

if __name__ == "__main__":
    app.run(debug=True)