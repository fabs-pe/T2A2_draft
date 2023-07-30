from flask import Blueprint, request
from init import db
from models.artist import Artist, artist_schema, artists_schema
from models.song import Song,song_schema, songs_schema
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required

artists_bp = Blueprint('artists', __name__, url_prefix = '/artists')

# Get all artists
@artists_bp.route('/', methods =['GET'])
def get_all_artists():
    stmt = db.select(Artist)
    artists =db.session.scalars(stmt)
    return artists_schema.dump(artists)

#  Get one artist by id
@artists_bp.route('/<int:id>', methods =['GET'])
def get_one_artist(id):
    stmt = db.select(Artist).filter_by(id=id) 
    artist = db.session.scalar(stmt)
    if artist:
        return artist_schema.dump(artist)
    else:
        return{'error': f'Artist with id {id} not found'}
    
# Create a new artist model instance
@artists_bp.route('/', methods = ['POST'])
@jwt_required()
def create_artist():
    body_data = request.get_json()
    artist = Artist(
        artist_name = body_data.get('artist_name'),
        country = body_data.get('country'),
    )
    db.session.add(artist) # add new data to database
    db.session.commit()

    return artist_schema.dump(artist), 201 # return data

# Add Song to db with artist id
@artists_bp.route('/<int:artist_id>', methods = ['POST'])
@jwt_required()
def add_song(artist_id):
    body_data = request.get_json()
    stmt =  db.select(Artist)
    artist = db.session.scalar(stmt)
    if artist:
        song = Song(
            title = body_data.get('title'), # song fields
            genre = body_data.get('genre'), # song fields
            artist_id = artist_id
        )

        db.session.add(song)
        db.session.commit()
        return artist_schema.dump(song), 201 # returns new son id
    else:
        return {'error': f'Artist not found with id {artist_id}'}, 404
    

# Delete Artist by id
@artists_bp.route('/<int:id>', methods =['DELETE'])
@jwt_required()
def delete_one_artist(id):
    is_admin = authorise_as_admin() #check if user is admin
    if not is_admin:
        return {'error' : 'Not authorised to delete artists'}, 403
    stmt =db.select(Artist). filter_by(id=id) #excutes if user is admin
    artist = db.session.scalar(stmt)
    if artist:
        db.session.delete(artist)
        db.session.commit()
        return {'message': f'{artist.artist_name} has been deleted successfully'} # let user know artist was deleted
    else:
        return {'error' : f'Artist not found with id {id}'}, 404 # let user know that the artist doesnt exist
    
# Edit Artist
@artists_bp.route('/<int:id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_artist(id):
    is_admin = authorise_as_admin() # check to see if user is admin function
    if not is_admin:
        return {'error' : 'Not authorised to edit artists'}, 403
    body_data = request.get_json() #excutes if user is admin
    stmt = db.select(Artist).filter_by(id =id)  # Select * from Artist where id = id
    artist = db.session.scalar(stmt)
    if artist:
        artist.artist_name = body_data.get('artist_name') or artist.artist_name # entries that can edited
        artist.country = body_data.get('country') or artist.country # entries that can edited
        db.session.commit()
        return artist_schema.dump(artist)
    
    else: 
        return {'error' : f'Artist with id {id} not found'}, 404  # Id not found to be deleted
    

# will authorise if user is admin by checking if user. is_admin = True
def authorise_as_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id= user_id)
    user = db.session.scalar(stmt)
    return user.is_admin
    

    