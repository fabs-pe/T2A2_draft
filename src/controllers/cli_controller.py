from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.playlist import Playlist
from models.song import Song
from models.artist import Artist
from models.song_list import Songlist
from datetime import date

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users =[
        User(
            name= 'admin',
            email='admin@theboss.com',
            password=bcrypt.generate_password_hash('admin2417').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='John Smith',
            email='johns@company.com',
            password=bcrypt.generate_password_hash('password12').decode('utf-8')
        ),
        User(
            name='Biance Jones',
            email= 'biance@company.com',
            password=bcrypt.generate_password_hash('password12').decode('utf-8')
        ),
        User(
            name ='Sally Turner',
            email='sally@company.com',
            password=bcrypt.generate_password_hash('password12').decode('utf-8')

        ),
        User(
            name= 'Scott User',
            email= 'scott@mail.com',
            password= bcrypt.generate_password_hash('pasword12').decode('utf-8')
        )
    ]

    db.session.add_all(users)

    playlists =[
        Playlist(
            title='Work',
            date_created = date.today(),
            description= 'Work Safe Music',
            user =users[0]
        ),
        Playlist(
            title = 'Pre-drinks',
            date_created = date.today(),
            description = 'Get me pumped',
            user = users[0]
        ),
        Playlist(
            title= 'Gym',
            date_created= date.today(),
            user =users[4]
        ),
        Playlist(
            title = 'Sleep',
            date_created= date.today(),
            user =users[0]
        ),
        Playlist(
            title = '40th Party',
            date_created = date.today(),
            description = 'Scotts Favourites',
            user =users[0]
        ),
        Playlist(
            title = '70s',
            date_created = date.today(),
            user = users[2]
        ),
        Playlist(
            title = 'Todays Hits',
            date_created = date.today(),
            description = 'Latest and Best',
            user = users[3]
        ),
        Playlist(
            title = 'Road Trip',
            date_created = date.today(),
            description = 'Sing along fun',
            user = users[4] 
        )
    ]
    db.session.add_all(playlists)


    artists =[
        Artist(
            artist_name = 'Usher',
            country = 'America'
        ),
        Artist(
            artist_name = 'INXS',
            country = 'Australia'
        ),
        Artist(
            artist_name = 'Travis Scott',
            country = 'America'
        ),
        Artist(
            artist_name = 'David Guetta',
            country = 'France'
        ),
        Artist(
            artist_name = 'ABBA',
            country = 'Sweden' 
        ),
        Artist(
            artist_name = 'Rod Stewart',
            country = 'England'
        ),
        Artist(
            artist_name = 'Fleetwood Mac',
            country ='England'
        ),
        Artist(
            artist_name = 'Calvin Harris',
            country = 'Scotland'
        ),
        Artist(
            artist_name ='Sneaky Sound System',
            country = 'Australia'
        ),
    ]
    db.session.add_all(artists)

    songs =[
        Song(
            title ='The way it is',
            genre = 'RnB',
            artist = artists[0]
        ),
        Song(
            title = 'Yeah',
            genre = 'RnB',
            artist = artists[0]
        ),
        Song(
            title = 'Dj Got Us Fallin  in Love',
            genre = 'RnB',
            artist = artists[0]
        ),
        Song(
            title = 'Never Tear Us Apart',
            genre = 'Rock',
            artist = artists[1]
        ),
        Song(
            title = 'Suicide Blonde',
            genre = 'Rock',
            artist = artists[1]
        ),
        Song(
            title = 'Goosebumps',
            genre = 'Pop',
            artist = artists[2]
        ),
        Song(
            title ='Star Gazing',
            genre ='Dance',
            artist = artists[2]
        ),
        Song(
            title = 'Say My Name',
            genre = 'Dance',
            artist = artists[3]
        ),
        Song(
            title = 'When Love Takes Over',
            genre = 'Pop',
            artist = artists[3]
        ),
        Song(
            title = 'Whos That Chick',
            genre = 'Dance',
            artist = artists[3]
        ),
        Song(
            title = 'Sexy Chick',
            genre = 'Pop',
            artist =artists[3]
        ),
        Song(
            title = 'Lay All Your Love On Me',
            genre = '70s',
            artist = artists[4]
        ),
        Song(
            title = 'Money, Money, Money',
            genre = '70s',
            artist = artists[4]
        ),
        Song(
            title = 'Gimme, Gimme, Gimme',
            genre = '70s',
            artist = artists[4]
        ),
        Song(
            title = 'Sailing',
            genre = '70s',
            artist = artists[5]
        ),
        Song(
            title ='Forver Young',
            genre = '70s',
            artist = artists[5]
        ),
        Song(
            title = 'Dreams',
            genre = '70s',
            artist = artists[6]
        ),
        Song(
            title = 'Little Lies',
            genre = '70s',
            artist = artists[6]
        ),
        Song(
            title = 'Landslide',
            genre = '70s',
            artist = artists[6]
        ),
        Song(
            title = 'My Way',
            genre = 'Dance',
            artist = artists[7]
        ),
        Song(
            title = 'Acceptable in the 80s',
            genre = 'Dance',
            artist = artists[7]
        ),
        Song(
            title = 'New To You',
            genre = 'Pop',
            artist = artists[7]
        ),
        Song(
            title = 'UFO',
            genre ='Dance',
            artist = artists[8]
        ),
        Song(
            title = 'Pictures',
            genre = 'Pop',
            artist = artists[8]
        )
    ]
    db.session.add_all(songs)

    songlists =[
        Songlist(
            song = songs[2],
            playlist = playlists[0]
        ),
        Songlist(
            song = songs[7],
            playlist = playlists[0]
        ),
        Songlist(
            song = songs[20],
            playlist = playlists[0]
        ),
        Songlist(
            song = songs[22],
            playlist = playlists[0]
        ),
        Songlist(
            song = songs[23],
            playlist = playlists[1]
        ), 
        Songlist(
            song = songs[20],
            playlist = playlists[1]
        ),
        Songlist(
            song = songs[9],
            playlist = playlists[1]
        ),
        Songlist(
            song = songs[2],
            playlist = playlists[1]
        ),
        Songlist(
            song = songs[22],
            playlist = playlists[2]
        ),
        Songlist(
            song = songs[19],
            playlist = playlists[2]
        ),
        Songlist(
            song = songs[10],
            playlist = playlists[2]
        ),
        Songlist(
            song = songs[5],
            playlist = playlists[2]
        ),
        Songlist(
            song = songs[0],
            playlist = playlists[3]
        ),
        Songlist(
            song = songs[14],
            playlist = playlists[3]
        ),
        Songlist(
            song = songs[18],
            playlist = playlists[3]
        ),
        Songlist(
            song = songs[23],
            playlist = playlists[4]
        ),
        Songlist(
            song = songs[22],
            playlist = playlists[4]
        ),
        Songlist(
            song = songs[9],
            playlist = playlists[4]
        ),
        Songlist(
            song = songs[8],
            playlist = playlists[4]
        ),
        Songlist(
            song = songs[11],
            playlist = playlists[5]
        ),
        Songlist(
            song = songs[12],
            playlist = playlists[5]
        ),
        Songlist(
            song = songs[13],
            playlist = playlists[5]
        ),
        Songlist(
            song = songs[14],
            playlist = playlists[5]
        ),
        Songlist(
            song = songs[15],
            playlist = playlists[5]
        ), 
        Songlist(
            song = songs[2],
            playlist = playlists[6]
        ),
        Songlist(
            song = songs[3],
            playlist = playlists[6]
        ),
        Songlist(
            song = songs[0],
            playlist = playlists[6]
        ),
        Songlist(
            song = songs[6],
            playlist = playlists[6]
        ),
        Songlist(
            song = songs[22],
            playlist = playlists[7]
        ),
        Songlist(
            song = songs[19],
            playlist = playlists[7]
        ),
        Songlist(
            song = songs[13],
            playlist = playlists[7]
        ),
        Songlist(
            song = songs[11],
            playlist = playlists[7]
        ),                
    ]
    db.session.add_all(songlists)

    db.session.commit()


    print("Tables seeded")