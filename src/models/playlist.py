from init import db, ma 
from marshmallow import fields, validates 
from marshmallow.validate import Length, And, Regexp, OneOf
from marshmallow.exceptions import ValidationError



class Playlist(db.Model):
    __tablename__ = 'playlists'

    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    date_created = db.Column(db.Date) # Date created
    description = db.Column(db.String(50))
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    
    user = db.relationship('User', back_populates='playlists')
    songlists = db.relationship('Songlist', back_populates='playlist',  cascade='all, delete')
    

class PlaylistSchema(ma.Schema):
    user = fields.Nested('UserSchema', only = ['name', 'email']) # joins user fields to playlist
    songlists = fields.List(fields.Nested('SonglistSchema'), only= ['song'])

    title = fields.String(required=True, validate=And(
        Length(min=2, error='Title must be at least 2 characters long'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, spaces and numbers are allowed')
    ))

    class Meta:
        fields = ('id','title', 'date_created', 'description', 'songlists')
        ordered = True

playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)


