from flask import Flask
from config import Config
from models import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)
CORS(app)

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.vote import vote_bp
from routes.results import results_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(vote_bp, url_prefix='/vote')
app.register_blueprint(results_bp, url_prefix='/results')

if __name__ == "__main__":
    app.run(debug=True)