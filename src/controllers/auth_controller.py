from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, user_schema, users_schema
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import get_jwt_identity, jwt_required


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
    

#list users. Admin only
@auth_bp.route('/users', methods =['GET'])
@jwt_required()
def get_all_users():
    is_admin = authorise_as_admin() # check to see if user is admin function
    if not is_admin:
        return {'error' : 'Not authorised to view users'}, 403
    stmt = db.select(User)
    users =db.session.scalars(stmt)
    return users_schema.dump(users)

#  Get one user by id
@auth_bp.route('users/<int:id>', methods =['GET'])
@jwt_required()
def get_one_user(id):
    is_admin = authorise_as_admin() # check to see if user is admin function
    if not is_admin:
        return {'error' : 'Not authorised to view users'}, 403
    stmt = db.select(User).filter_by(id=id) 
    user = db.session.scalar(stmt)
    if user:
        return user_schema.dump(user)
    else:
        return{'error': f'User with id {id} not found'}
    

# delete users. Admin Only
@auth_bp.route('/delete/<int:id>', methods =['DELETE'])
@jwt_required()
def delete_one_user(id):
    is_admin = authorise_as_admin() #check if user is admin
    if not is_admin:
        return {'error' : 'Not authorised to delete users'}, 403
    stmt =db.select(User). filter_by(id=id) #excutes if user is admin
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f'{user.id} has been deleted successfully'} # let admin know user was deleted
    else:
        return {'error' : f'User not found with id {id}'}, 404 # let admin know that the user doesnt exist
    
# Edit User. Can only edit own profile
@auth_bp.route('/<int:id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_user(id):
    body_data = request.get_json() #excutes if user is admin
    stmt = db.select(User).filter_by(id =id)  # Select * from User where id = id
    user= db.session.scalar(stmt)
    if user:
        if str(user.id) != get_jwt_identity():
            return { 'error' : 'Only the owner of the profile can make changes'}, 403
        user.name = body_data.get('name') or user.name # entries that can edited
        user.email = body_data.get('email') or user.email # entries that can edited
        user.password = body_data.get('password') or user.password # entries that can edited
        db.session.commit()
        return user_schema.dump(user)
    
    else: 
        return {'error' : f'User with id {id} not found'}, 404  # Id not found to be deleted

# will authorise if user is admin by checking if user. is_admin = True
def authorise_as_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id= user_id)
    user = db.session.scalar(stmt)
    return user.is_admin       
