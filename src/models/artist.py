from init import db, ma
from marshmallow import fields

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(50))
    country = db.Column(db.String(50))

    
    songs =db.relationship('Song', back_populates='artist',  cascade='all, delete')

class ArtistSchema(ma.Schema):
    songs = fields.List(fields.Nested('SongSchema', only= ['title', 'genre']))
    
    class Meta:
        fields= ('id', 'artist_name', 'country', 'songs')
        ordered = True

artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True) 