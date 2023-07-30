from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, user_schema, users_schema
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes
from sqlalchemy.exc import IntegrityError
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix ='/auth')

# Register Route
@auth_bp.route('/register', methods =['POST'])
def auth_register():
    try:
        body_data = request.get_json()

        # Create a new User model instance from the user info
        user = User()
        user.name = body_data.get('name')
        user.email = body_data.get('email')
        if body_data.get('password'):
            # decode- convert from bytes to utf format
            user.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')
        # add and commit the user to the session
        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user), 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return { 'error': 'Email address already in use, try again' }, 409
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return { 'error': f'The {err.orig.diag.column_name} is required' }, 409

# Login Route
@auth_bp.route('/login', methods=['POST'])
def auth_login():
    body_data = request.get_json()
    # Use email address
    stmt = db.select(User).filter_by(email = body_data.get('email'))
    user = db.session.scalar(stmt)
    # check if the user exists and the password is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get('password')):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1)) # password token expires
        return {'email' : user.email, 'token' : token, 'is_admin' : user.is_admin}
    else:
        return { 'error' : 'Invalid email or password'}, 401
                                                  
