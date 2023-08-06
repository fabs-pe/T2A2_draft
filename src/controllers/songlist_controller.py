from flask import Blueprint, request
from init import db
from models.song_list import Songlist, songlist_schema, songlists_schema
from models.playlist import Playlist, playlist_schema
from models.song import Song
from flask_jwt_extended import get_jwt_identity, jwt_required
from datetime import date

songlists_bp = Blueprint('songlists', __name__, url_prefix='/songlists')


@songlists_bp.route('/', methods =['GET'])
def get_all_lists():
    stmt = db.select(Songlist)
    songlists = db.session.scalars(stmt)
    return songlists_schema.dump(songlists)

@songlists_bp.route('/<int:id>', methods =['GET'])
def get_one_list(id):
    stmt = db.select(Songlist).filter_by(id=id)
    songlist = db.session.scalar(stmt)
    if songlist:
        return songlist_schema.dump(songlist)
    else:
        return {'error': f'Songlist not found with id {id}'}, 404
    

# Create new songlist model Instance
@songlists_bp.route('/', methods = ['POST'])
@jwt_required()
def create_songlist():
    body_data = request.get_json()
    playlist = Playlist(
        user_id = get_jwt_identity(),
        title = body_data.get('title'),
        description = body_data.get('description'),
        date_created = date.today()
    )
    db.session.add(playlist)
    db.session.commit()

    return playlist_schema.dump(playlist), 201
    
@songlists_bp.route('/addsong/<int:id>', methods = ['POST'])
@jwt_required()
def song_to_list(id):
    body_data = request.get_json()
    songlist = Songlist(
        song_id = body_data.get('song_id'),
        playlist_id = body_data.get('playlist_id'),
    )
    db.session.add(songlist) # add new data to database
    db.session.commit()

    return songlist_schema.dump(songlist), 201 # return data

    

    
