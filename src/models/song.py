from init import db, ma 
from marshmallow import fields, validates 
from marshmallow.validate import Length, And, Regexp, OneOf
from marshmallow.exceptions import ValidationError


VALID_GENRE = ('Dance', 'RnB', 'Rock', '70s', 'Pop')


class Song(db.Model):
    __tablename__ = 'songs'

    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    
    artist = db.relationship('Artist', back_populates='songs')
    songlists = db.relationship('Songlist', back_populates='song',  cascade='all, delete')

class SongSchema(ma.Schema):
    artist = fields.Nested('ArtistSchema', only = ['artist_name', 'country']) # joins 
    songlists = fields.List(fields.Nested('SonglistSchema'))

    genre = fields.String(validate=OneOf(VALID_GENRE))

    class Meta:
        fields = ('id','title', 'genre', 'artist', 'songlists')
        ordered = True

song_schema = SongSchema()
songs_schema = SongSchema(many=True)