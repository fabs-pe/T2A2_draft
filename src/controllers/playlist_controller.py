from flask import Blueprint, request
from init import db
from models.playlist import Playlist, playlists_schema, playlist_schema
from models.song import Song, song_schema, songs_schema
from models.artist import Artist
from models.user import User
from datetime import date
from flask_jwt_extended import get_jwt_identity, jwt_required

playlists_bp = Blueprint('playlists', __name__, url_prefix = '/playlists')

# get all playlists
@playlists_bp.route('/', methods =['GET'])
def get_all_playlists():
    stmt = db.select(Playlist).order_by(Playlist.date_created.desc())
    playlists = db.session.scalars(stmt)
    return playlists_schema.dump(playlists)

# Get one Playlist using playlist_id
@playlists_bp.route('/<int:id>', methods =['GET'])
def get_one_playlist(id):
    stmt = db.select(Playlist).filter_by(id=id)
    playlist = db.session.scalar(stmt)
    if playlist:
        return playlist_schema.dump(playlist)
    else:
        return {'error': f'Playlist not found with id {id}'}, 404
    
# Create new Playlist model Instance
@playlists_bp.route('/', methods = ['POST'])
@jwt_required()
def create_playlist():
    body_data = playlist_schema.load(request.get_json())
    playlist = Playlist(
        user_id = get_jwt_identity(),
        title = body_data.get('title'),
        description = body_data.get('description'),
        date_created = date.today()
    )
    db.session.add(playlist)
    db.session.commit()

    return playlist_schema.dump(playlist), 201

# Delete a playlist by playlist_id
@playlists_bp.route('/<int:id>', methods =['DELETE'])
@jwt_required()
def delete_one_playlist(id):
    stmt =db.select(Playlist). filter_by(id=id)
    playlist = db.session.scalar(stmt)
    if playlist:
        if str(playlist.user_id) != get_jwt_identity():
            return { 'error' : 'Only the owner of the playlist can delete it.'}, 403
        db.session.delete(playlist)
        db.session.commit()
        return {'message': f'Playlist {playlist.title} deleted successfully'}
    else:
        return {'error' : f'Playlist not found with id {id}'}, 404
    
# Edit a playlist
@playlists_bp.route('/<int:id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_one_playlist(id):
    body_data = playlist_schema.load(request.get_json(), partial=True)
    stmt = db.select(Playlist).filter_by(id =id)  # Select * from Song where id = id
    playlist = db.session.scalar(stmt)
    if playlist:
        #  will get user id to compare with user FK in playlist
        if str(playlist.user_id) != get_jwt_identity():
            return { 'error' : 'Only the owner of the playlist can make changes'}, 403
        playlist.title = body_data.get('title') or playlist.title # entries that can edited
        playlist.description = body_data.get('description') or playlist.description # entries that can edited
        db.session.commit()
        return song_schema.dump(playlist)
    
    else: 
        return {'error' : f'Playlist with id {id} not found'}, 404  # Id not found to be deleted
    

# will authorise if user is admin by checking if user. is_admin = True
def authorise_as_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id= user_id)
    user = db.session.scalar(stmt)
    return user.is_admin
    
# Add Song to db with artist id
# @artists_bp.route('/<int:artist_id>', methods = ['POST'])
# @jwt_required()
# def add_song(artist_id):
#     body_data = request.get_json()
#     stmt =  db.select(Artist)
#     artist = db.session.scalar(stmt)
#     if artist:
#         song = Song(
#             title = body_data.get('title'), # song fields
#             genre = body_data.get('genre'), # song fields
#             artist_id = artist_id
#         )

#         db.session.add(song)
#         db.session.commit()
#         return artist_schema.dump(song), 201 # returns new son id
#     else:
#         return {'error': f'Artist not found with id {artist_id}'}, 404
    