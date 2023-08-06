from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id =db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50))
    email= db.Column(db.String(100), nullable=False, unique=True)
    password= db.Column(db.String(100), nullable=False)
    is_admin= db.Column(db.Boolean, default=False)

    playlists = db.relationship('Playlist', back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):
    playlists = fields.List(fields.Nested('PlaylistSchema', only= ['title']))
    
    class Meta:
        fields= ('id', 'name', 'email', 'password', 'is_admin', 'playlists')

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password']) 
