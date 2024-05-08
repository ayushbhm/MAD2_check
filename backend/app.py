from flask import Flask, jsonify,request
from flask_cors import CORS
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin,roles_required
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from itsdangerous import URLSafeTimedSerializer

from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"
jwt = JWTManager(app)

SECRET_KEY = 'your_secret_key'  


import sqlalchemy
from controllers.studenthome import studenthome_bp;
app.register_blueprint(studenthome_bp)
from controllers.authentication import authentication_bp;
app.register_blueprint(authentication_bp)

from controllers.admincontrols import admincontrols_bp;
app.register_blueprint(admincontrols_bp)

from models.models  import db, User, BookCategory, BookDetails, BookRating, BookRequests, BookReviews



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'

# Silence the deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)

from flask_cors import CORS 
CORS(app, origins='http://localhost:5173')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = User.query.filter_by(username=username).first()

    if users and users.password == password and any(role.name == 'student' for role in users.roles):
        token = create_access_token(identity=username)
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
    
    
@app.route('/AdminLogin', methods=['POST'])
def AdminLogin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    users = User.query.filter_by(username=username).first()

    if users and users.password == password and any(role.name == 'admin' for role in users.roles):
        token = create_access_token(identity=username)
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
    
    
    
    
    
    
    
    
    
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()

    new_request = User(
    username=username,
    password = password
    )
    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'register requested successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500
        






# Routes
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Flask+SQLite API!'})



@app.route('/check_database_connection')
def check_database_connection():
    # Access and print the database URI
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    return f'Connected to database: {database_uri}'





if __name__ == '__main__':
   
    with app.app_context():
        db.create_all()
    app.run(debug=True)
