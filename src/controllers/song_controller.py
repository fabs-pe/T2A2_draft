from flask import Blueprint, request
from init import db
from models.song import Song, songs_schema, song_schema
from models.artist import Artist, artist_schema, artists_schema
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required



songs_bp = Blueprint('songs', __name__, url_prefix='/songs')

# Get all songs
@songs_bp.route('/', methods =['GET'])
def get_all_songs():
    stmt = db.select(Song).order_by(Song.genre.desc())
    songs = db.session.scalars(stmt)
    return songs_schema.dump(songs)

# Get one song by using id
@songs_bp.route('/<int:id>', methods =['GET']) 
def get_one_song(id):
    stmt = db.select(Song).filter_by(id=id)
    song = db.session.scalar(stmt)
    if song:
        return song_schema.dump(song)  # display song with matching id
    else:
        return {'error': f'Song not found with id {id}'}, 404  # catch error if id is not found
    
# Create new Song Model Instance
@songs_bp.route('/', methods = ['POST'])
@jwt_required()
def create_song():
    is_admin = authorise_as_admin()
    if not is_admin:
        return {'error' : 'Not authorised to delete songs'}, 403
    body_data = request.get_json()
    song = Song(
        genre = body_data.get('genre'),
        title = body_data.get('title'),
        artist_id = body_data.get('artist_id')
    )
    db.session.add(song) # add new data to database
    db.session.commit()

    return song_schema.dump(song), 201 #return data

# Delete a single song
@songs_bp.route('/<int:id>', methods =['DELETE']) # the id of song to be deleted
@jwt_required()
def delete_one_song(id):
    is_admin = authorise_as_admin()
    if not is_admin:
        return {'error' : 'Not authorised to delete songs'}, 403
    
    stmt =db.select(Song). filter_by(id=id)
    song = db.session.scalar(stmt)
    if song:
        db.session.delete(song)
        db.session.commit()
        return {'message': f'Song - {song.title} with id {song.id} deleted successfully'} # Confirm that song was deleted successfully
    else:
        return {'error' : f'Song not found with id {id}'}, 404 # let client know the id doesnt exist
    

# Edit a song
@songs_bp.route('/<int:id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_song(id):
    is_admin = authorise_as_admin()
    if not is_admin:
        return {'error' : 'Not authorised to edit songs'}, 403
    
    body_data = song_schema.load(request.get_json(), partial=True)
    stmt = db.select(Song).filter_by(id =id)  # Select * from Song where id = id
    song = db.session.scalar(stmt)
    if song:
        song.title = body_data.get('title') or song.title # entries that can edited
        song.genre = body_data.get('genre') or song.genre # entries that can edited
        song.artist.id = body_data.get('artist_id') or song.artist.id
        
        db.session.commit()
        return song_schema.dump(song)
    
    else: 
        return {'error' : f'Song with id {id} not found'}, 404  # Id not found to be deleted
    
# will authorise if user is admin by checking if user. is_admin = True
def authorise_as_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id= user_id)
    user = db.session.scalar(stmt)
    return user.is_admin
    

    
    
    
  
