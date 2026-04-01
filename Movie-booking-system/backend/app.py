from flask import Flask
from flask_cors import CORS
from config import Config
from models import db

from routes.movie_routes import movie_bp
from routes.booking_routes import booking_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)

app.register_blueprint(movie_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(admin_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)