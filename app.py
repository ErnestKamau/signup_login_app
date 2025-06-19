from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True
CORS(app)
migrate = Migrate(app, db)
db.init_app(app)

app.route('/')
def index():
    return jsonify({"message": "Welcome to the User API"}), 200
    
# @app.route('/users', methods=['GET'])
# def signup():
#     try:
#         d



if __name__ == '__main__':
    app.run(port=5555 ,debug=True)