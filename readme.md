# Playlist Api Web Server

## **Installation and Setup**

- Create a folder locally to store the API. 
- Download the repository from Github.

```postgresql

CREATE DATABASE playlist_api;
\c vinyl_data_api_db;
CREATE USER list_dev WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE playlist_api TO list_dev;
GRANT ALL ON SCHEMA public to list_dev;

```

Next head over to [GitHub](https://github.com/fabs-pe/T2A2_draft) to down the code needed for the API.

Select "Download Zip" from the green "CODE" button.

A Virtual Enviroment needs to be created. The '.' will make this a hidden file.

```
python3 -m venv .play-venv
```

Activate the enviroment

``` 
source play-venv/bin/activate
```
Install the requirements.txt file
```
pip install -r requirements.txt
```

Create a .env file at the root of the project with the following contents:
```
DATABASE_URL="postgresql+psycopg2://list_dev:1234@localhost:5432/playlist_api"
JWT_SECRET_KEY="playkey"
```

Create and seed the database then run the Flask application with the following cli commands:
```
flask db create
flask db seed
flask run
```


## R1 	Identification of the problem you are trying to solve by building this particular app.

The problem that this app will solve is it will giev the user a menas of sorting music into multiple playlists. The user can create an account and many playlists with unlimited songs in each playlist. Once created only the owner of th list can edit and delete it. The user will need to be logged in to be able to do this. Only users with admin rights will be able to update the songs and artists models. Admin rights are also needed to delete users.

## R2 Why is it a problem that needs solving?

Having music on an app, with your own account on multiple devices is very useful for any situation they music may be needed, eg - work, gym, road trips,parties.
A playlist can be created for each of these events and used with use at any given time. This can be a time saver and making listening to music easy and quick.

## R3 Why have you chosen this database system. What are the drawbacks compared to others?

PostgreSQL is a powerful open-source relational database system. PostgreSQL offers cutting-edge functionality and dependability. It is robust and stable. PostgreSQL also has a reputation for being highly reliable with a strong focus on consistency and data integrity. Features like ACID(Atomicity, Consistency, Isolation, Durability) properties help ensure the integrity of data. PostgreSQL is designed to handle large amounts of data and high levels of traffic loads. Because it supports scalability features such has table partitioning, replication & clustering it makes it suitable for growing web applications. PostgreSQL has efficient handling of JSON documents in the database. A great advantage is the large and active community of users and developers, leading to large amounts of resources, documentation and support of the community. 

For all the great advantages there are also some disadvantages, such has the learning curve and configuration options. This can be overwhelming at times. Additional work is needed for proper configuration to achieve optimal performance. 
PostgreSQL has a memory management that can be demanding when dealing with larger datasets.

PostgreSQL is a mature relational database known for structured data and ACID compliance, ideal for complex queries and critical applications like finance and e-commerce. MongoDB, a NoSQL document-oriented database, offers schema flexibility, making it suitable for projects with dynamic or unstructured data, such as web apps, real-time analytics, and IoT applications. PostgreSQL excels in vertical scaling, while MongoDB natively supports horizontal scalability. The choice depends on the project's specific requirements, data structure, and need for transactions. PostgreSQL has a long-standing community, while MongoDB's community and ecosystem are rapidly growing. Consider the trade-offs of each system before deciding on the best fit.

## R4 Identify and discuss the key functionalities and benefits of an ORM


An Object-Relational Mapping (ORM) is a powerful software tool that bridges the gap between object-oriented programming languages and relational databases. Its key functionalities and benefits are as follows:

- Database operations are abstracted by ORM, which enables programmers to write high-level object-oriented code by abstracting the low-level database interactions. This makes database management easier and eliminates the need for intricate SQL queries.

- Data Model Synchronisation: Based on the defined data models in the code, ORM tools automatically construct and synchronise the database schema. As a result, there is no longer a need for manual database schema upgrades, and the application and database are consistent.

- Increased Productivity: Instead of dealing with database complexities, developers may concentrate on application logic and business requirements. This increases output, quickens the pace of development, and lowers the likelihood of mistakes.

- Security: By handling parameterization and data escaping automatically, ORM helps eliminate widespread security problems like SQL injection.

- Refactoring and Maintainability: With ORM, developers may quickly change data models and associations without changing SQL queries throughout the entire codebase, improving maintainability and promoting agile development practises.

- Built-in Caching and Optimisation: ORM frequently comes with built-in caching mechanisms and query optimisation techniques, which can greatly enhance application speed by lowering database round-trips.

In conclusion, an ORM is a valuable tool that streamlines database interactions, enhances development productivity, improves application security, and contributes to the overall robustness and efficiency of software applications.

##  R5	Document all endpoints for your API

### User Endpoints 

<p align="center"> Auth Routes in Postman </p>
<p align="center"><img src="./docs/auth_routes.png" width = 50%></p>

## '/auth/users'

**METHODS : GET**

- Arguments: None
- Description: A route to list all users 
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)

<p align="center"> Error When User Not Admin </p>
<p align="center"><img src="./docs/view_users.png" width = 70%></p>

## '/auth/users/<int:id>'

**METHODS : GET**

- Arguments: Users id number
- Description: A route to list one id that matches called id
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)

## '/auth/register'

**METHODS: POST**

- Arguments: Users id number
- Description: register a new user into the database
- Authentication: None
- Authorization: None

**Request Body:**

This will create a user that is not admin

```json
{
   "name": "test user2",
    "email": "test@email3.com",
    "password" : "password"
    }

```
<p align="center"> Request Reponse </p>
<p align="center"><img src="./docs/user reg.png" width = 70%></p>

<p align="center"> Error When User try to register the same email </p>
<p align="center"><img src="./docs/already_reg.png" width = 70%></p>
<p align="center"> Error when not supplying email </p>
<p align="center"><img src="./docs/email req.png" width = 70%></p>

## '/auth/login'

**METHODS: POST**

- Arguments: None
- Description: route to login users/admin and receive a token to use for authentication and authorization
- Authentication: Email & Password
- Authorization: None

**Request Body:**

```json
{
    "email" : "admin@theboss.com",
    "password" : "admin2417"
}
```

**Reponse Body:**

```json
{
    "email": "admin@theboss.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MTMxNjgzNywianRpIjoiNDYwYTc5NWQtM2M4OS00ZmRjLWJjMzYtZGM2NWVhYjM1NzViIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE2OTEzMTY4MzcsImV4cCI6MTY5MTQwMzIzN30.6P7EAPBLYHMQbG3YFiWx_uWRc_MoGRzWHBkA4XbaHo0",
    "is_admin": true
}
```

## '/auth/delete/<int:id>'

**METHODS : DELETE**

- Arguments: user id  (integer) being searched for in URL
- Description: 
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)

<p align="center"> Deleting a user </p>
<p align="center"><img src="./docs/delete user.png" width = 70%></p>

## '/auth/delete/<int:id>'

**METHODS : PATCH PUT**

- Arguments: user id  (integer) being searched for in URL
- Description: route that allows a user to update their own profile
- Authentication: JWT Required
- Authorization: Bearer Token

**Request Body:**

```json
{
    "name" : "test 1 name",
    "email" : "test23@email",
    "password" : "newpassword"
}
```

**Reponse Body**

```json
{
    "name": "test 1 name",
    "id": 2,
    "email": "test23@email",
    "is_admin": false,
    "playlists": []
}
```
### Playlist Endpoints 

<p align="center"> Playlist Routes in Postman </p>
<p align="center"><img src="./docs/playlist_routes.png" width = 50%></p>

## '/playlists'

**METHODS : GET**

- Arguments: None
- Description: Route to display all playlists
- Authentication: None
- Authorization: None

<p align="center"> Results of Listing Playlists </p>
<p align="center"><img src="./docs/playlist_results.png" width = 70%></p>

## '/playlists/<int:id>'

**METHODS : GET**

- Arguments: playlist is being searched for in the URL
- Description: Route to display one playlists
- Authentication: None
- Authorization: None

## '/playlists'

**METHODS : POST**

- Arguments: None
- Description: Route to add one new playlists
- Authentication: None
- Authorization: Bearer Token (must be signed in)

**Request Body**

```Json
{
    "title" : "Test Playlist 133",
    "description" : "Test Description"
}
```

**Response Body**

```json
{
    "id": 13,
    "title": "Test Playlist 133",
    "date_created": "2023-08-08",
    "description": "Test Description",
    "songlists": []
}
```
# '/playlists/<int:id>'

**METHODS : PATCH**

- Arguments: playlist id being searched for in the URL
- Description: Route to edit a playlist owned by the user
- Authentication: JWT Required
- Authorization: Bearer Token

<p align="center"> Error When User try to edit a playlist thats doesnt belong to user </p>
<p align="center"><img src="./docs/owner_only.png" width = 70%></p>

## '/playlists/<int:id>'

**METHODS : DELETE**

- Arguments: playlist id  (integer) being searched for in URL
- Description: Route to delete a playlist
- Authentication: JWT Required
- Authorization: Bearer Token

<p align="center"> Success Message When playlist deleted </p>
<p align="center"><img src="./docs/delete_playlist.png" width = 70%></p>

<p align="center"> Error When Wrong User Tries To Delete A Playlist </p>
<p align="center"><img src="./docs/playlist_owner.png" width = 70%></p>

<p align="center"> Playlist Doesnt Exist </p>
<p align="center"><img src="./docs/delete_error.png" width = 70%></p>

## '/artists'

**METHODS : GET**

- Arguments: None
- Description: route that displays all artists and their songs
- Authentication: None
- Authorization: None

<p align="center"> List of artists </p>
<p align="center"><img src="./docs/artist_list.png" width = 70%></p>

## '/artists/<int:id>'

**METHODS : GET**

- Arguments: artist id (integer) being searched for in URL
- Description: route that displays one artists and their songs
- Authentication: None
- Authorization: None

<p align="center"> Error if artist id doesnt exist </p>
<p align="center"><img src="./docs/no_artist.png" width = 70%></p>

## '/artists'

**METHODS : POST**

- Arguments: None
- Description: route that allows an artists to be added to the database
- Authentication: JWT Required
- Authorization: Bearer Token

**Request Body**

```json
{
    "artist_name": " final test artist ",
    "country" : "test country 3"
}
```

<p align="center"> Error if user is an admin </p>
<p align="center"><img src="./docs/not_added_artist.png" width = 70%></p>

## '/artists/addsong/<int:id>'

**METHODS : POST**

- Arguments: artist id of the artist for the song to added too
- Description: route that allows a song be added to an artist
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)

**Request Body**

```json
{
    "title": " final test artist ",
    "genre": "test country 4"
    
}
```
**Response Body**

```json
{
    "id": 1,
    "artist_name": "Usher",
    "country": "America",
    "songs": [
        {
            "title": " final test artist ",
            "genre": "test country 3"
        },
        {
            "title": " final test artist ",
            "genre": "test country 4"
        }
    ]
}
```
## '/artists/<int:id>'

**METHODS : PATCH**

- Arguments: artist id  (integer) being searched for in URL
- Description: Edit an artists details
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)


**Request Body**

```json
{
    "artist_name" : "Name edited",
    "country" : "country edited"
}
```
<p align="center"> Error When Non Admin tries to edit artist </p>
<p align="center"><img src="./docs/not_auth_artist.png" width = 70%></p>

## '/artists/<int:id>'

**METHODS : DELETE**

- Arguments: artist id  (integer) being searched for in URL
- Description: delete an artists 
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)

<p align="center"> Error When Non Admin tries to delete an artist </p>
<p align="center"><img src="./docs/not_auth_delete.png" width = 70%></p>

<p align="center"> Successfully Deleted </p>
<p align="center"><img src="./docs/delete_success.png" width = 70%></p>

### Song Endpoints 

<p align="center"> Song Routes in Postman </p>
<p align="center"><img src="./docs/song_routes.png" width = 50%></p>

## '/songs'

**METHODS : GET**

- Arguments: None
- Description: route that displays all songs
- Authentication: None
- Authorization: None

<p align="center"> Display All Songs </p>
<p align="center"><img src="./docs/songs_display.png" width = 50%></p>

## '/songs/<int:id>'

**METHODS : GET**

- Arguments: song id (integer) being searched for in URL
- Description: route that displays one songs
- Authentication: None
- Authorization: None

<p align="center"> Display Song and playlist that its in </p>
<p align="center"><img src="./docs/one_song.png" width = 50%></p>

<p align="center"> Error: Song id not found </p>
<p align="center"><img src="./docs/no_song.png" width = 50%></p>

## '/song/<int:id>'

**METHODS : DELETE**

- Arguments: song id  (integer) being searched for in URL
- Description: delete a song 
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)

<p align="center"> Song Successfully Deleted </p>
<p align="center"><img src="./docs/song_deleted.png" width = 50%></p>

<p align="center"> Song Not Found </p>
<p align="center"><img src="./docs/not_delete_song.png" width = 50%></p>

<p align="center"> Not Auth To Delete </p>
<p align="center"><img src="./docs/no_auth_song.png" width = 50%></p>

## '/song'

**METHODS : POST**

- Arguments: None
- Description: Route to add a song
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)

**Request Body**

```json
{
    "title" : "test playlist",
    "genre" : " test list",
    "artist_id" : "10"

}

```

**Response Body**

```json
{
    "id": 33,
    "title": "test playlist",
    "genre": " test list",
    "artist": {
        "artist_name": null,
        "country": null
    },
    "songlists": []
}

```

## '/song/<int:id>'

**METHODS : PATCH**

- Arguments: song id (integer) being searched for in URL
- Description: Route to edit a song
- Authentication: JWT Required
- Authorization: Must be admin (Bearer Token)

**Request Body**

```json
{
    "title" : "test song edited",
    "genre" : "Pop"
}
```

**Response Body**

```json
{
    "id": 8,
    "title": "test song edited",
    "genre": "Pop",
    "artist": {
        "artist_name": "David Guetta",
        "country": "France",
        "id": 4
    },
    "songlists": [
        {
            "id": 2,
            "playlist": {
                "id": 1,
                "title": "Work",
                "description": "Work Safe Music"
            },
            "song": {
                "id": 8,
                "title": "test song edited",
                "genre": "Pop",
                "artist": {
                    "artist_name": "David Guetta",
                    "country": "France",
                    "id": 4
                }
            }
        }
    ]
}

```

### Songlist Endpoints 

<p align="center"> Songlist Routes in Postman </p>
<p align="center"><img src="./docs/songlist_routes.png" width = 50%></p>

## '/songlists'

**METHODS : GET**

- Arguments: None
- Description: Route to display songs in a playlist id
- Authentication: None
- Authorization: Bearer Token

<p align="center"> Displays Each Playlisy with each song </p>
<p align="center"><img src="./docs/all_songlists.png" width = 50%></p>

## '/songlists/<int:id>'

- Arguments: songlist id
- Description: Route to display one playlist with songs 
- Authentication: None
- Authorization: Bearer Token

```json
{
    "id": 2,
    "title": "Pre-drinks",
    "date_created": "2023-08-05",
    "description": "Get me pumped",
    "songlists": [
        {
            "id": 35,
            "playlist": {
                "id": 2,
                "title": "Pre-drinks",
                "description": "Get me pumped"
            },
            "song": {
                "id": 13,
                "title": "Money, Money, Money",
                "genre": "70s",
                "artist": {
                    "artist_name": "ABBA",
                    "country": "Sweden",
                    "id": 5
                }
            }
        },
        {
            "id": 36,
            "playlist": {
                "id": 2,
                "title": "Pre-drinks",
                "description": "Get me pumped"
            },
            "song": {
                "id": 15,
                "title": "Sailing",
                "genre": "70s",
                "artist": {
                    "artist_name": "Rod Stewart",
                    "country": "England",
                    "id": 6
                }
            }
        },
        {
            "id": 37,
            "playlist": {
                "id": 2,
                "title": "Pre-drinks",
                "description": "Get me pumped"
            },
            "song": {
                "id": 15,
                "title": "Sailing",
                "genre": "70s",
                "artist": {
                    "artist_name": "Rod Stewart",
                    "country": "England",
                    "id": 6
                }
            }
        }
    ]
}

```
## '/songlists'

**METHODS : POST**

- Arguments: None
- Description: Route to add song into a playlist id
- Authentication: None
- Authorization: Bearer Token

**Request Body**

```json
{
    "song_id" : "15",
    "playlist_id" : "2"
}
```

**Response Body**

```json
{
    "id": 37,
    "playlist": {
        "id": 2,
        "title": "Pre-drinks",
        "description": "Get me pumped"
    },
    "song": {
        "id": 15,
        "title": "Sailing",
        "genre": "70s",
        "artist": {
            "artist_name": "Rod Stewart",
            "country": "England",
            "id": 6
        }
    }
}
```



## R6 An ERD for your app

![ERD Image](/docs/Playlist_ERD.png)

## R7 Detail any third party services that your app will use

The below is a list of third party services that were used in this app.

**Psycopg2**

Psycopg2 is a multi-threaded application built PostgreSQL database driver that is used to conduct operations on PostgreSQL using Python. The execute() method in psycopg2 is used to run SQL queries. It is used to carry out a database action, command, or query.

Psycopg2 is used to connect to the PostgreSQL database and perform CRUD (Create, Read, Update, Delete) operations on the database tables. It allows the Python code to interact with the database using SQL commands, such as SELECT, INSERT, UPDATE, and DELETE.

**Marshmallow**

Marshmallow is a Python library that converts complex data types to and from Python data types. It is a powerful tool for both validating and converting data.

It makes it simple for the Python code to transform data from database tables into JSON format, which can then be provided through API endpoints. Flask-Marshmallow creates the JSON data that is delivered by the API endpoints by specifying schema classes that correspond to the database tables. As a result, the API can offer a constant and clearly defined data format that other programes and services can use.

**Flask Bcrypt**

Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities. it is uesd in the API for storing passwords of users securly.

![sample of password storage](/docs/bcrypt.png)

**JWT-Extended**

Flask-JWT-Extended adds support for using JSON Web Tokens (JWT) to Flask for protecting routes. 

The JWTs are signed with a key, and if someone gets their hands on it they will be able to create arbitrary tokens that are accepted by a web flask application.

**dotenv**

Developers can load environment variables from a.env file in the project directory using the Python module Python-Dotenv. By enabling programmers to keep confidential data apart from their code and to quickly transition between various environment configurations, this library streamlines the process of handling environment variables.

## R8 Describe your projects models in terms of the relationships they have with each other

The API consists of the following models
 - users
 - playlists
 - songs
 - artists
 - song_list

 **users**

 Each user can have many playlists. Users has a primary key of id which is used as a foreign key in the playlists model (user_id). When a playlist is created the user_id is stored back populates in the models. Using cascade command, if a user is deleted all playlists are related to that user_id are also deleted.

 **playlists**

 Each playlist can only have one user. Each playlist can have many songs. There for needs a many to many relation with songs, which is done with a join table(song_list). If a playlist is deleted, nothing else is deleted. because the two tables that have relationship with playlists (users, songs) are used in other relationships.

 **songs**

 Each song can only have one artist and but be in many playlists. If a song is deleted or updated the changes will be back populated in the artist and song_list models. An artist is not deleted if a song is deleted because an artist can have many songs.

 **artists**

The artist model has a FK of song_id. This is the only relatioship artist has. If an artist is deleted any song that use artist_id as a FK with that artist will also be deleted. When a new song from that artist is added it will back populate to reflect changes.

**song_list**

This is a join table for song and playlist

## R9 Discuss the database relations to be implemented in your application

**users**

This model represents a user of the API. Has on FK and has a one to many relationship with playlists. The following information is stored:

- id : is a primary key with an auto incrementing integer value
- name : a string with a maximium of 50 characters
- email : a string with a maximium of 50 characters, can not be null and must be uniquie.
- password : saved using bcrypt and coverted to utf-8

**playlists**

This represents all the  playlist. Has a one to many relationship with users (one user pre playlist) and many to many with songs, using a one to many with song_list (join table)
- id : is a primary key with an auto incrementing integer value
- title : a string with a maximium of 50 characters
- description : a string with a maximium of 50 characters
- date_created: use datetime to record date created
- FK : users_id

**songs**

This reresents all the available songs. Has a one to many relatioship with artists and a many to many with playlists, using a one to many with song_list (join table)
- id : is a primary key with an auto incrementing integer value
- title : a string with a maximium of 50 characters
- genre : : a string with a maximium of 50 characters but has to meet validation
- FK : artist_id
![genre validation](/docs/genre.png)

**artists**

This represents all the artist. Has a one to many relatioship with songs. Each song can only hve one artist, and each artist can have one or many songs.
- id : is a primary key with an auto incrementing integer value
- artist_name : a string with a maximium of 50 characters
- country : a string with a maximium of 50 characters
- FK : song_id

**song_list**

This is a join table for the playlists and songs models
- id : is a primary key with an auto incrementing integer value
- FK : song_id
- FK : playlist_id

![relationship](/docs/song_playlist.png)

## R10 Describe the way tasks are allocated and tracked in your project

 **[Trello Board](https://trello.com/invite/b/4o8NzsAY/ATTI0e87f71eb1a113d3eac88988c4f101d5D53B6284/playlist-api)**

 Trello was used to plan and track progress of the API

 I used 4 boards 
 - To Do
 - Doing
 - Done
 - On going

 The cards were moved into the appropriate stages each time I revisited the Trello board.

 I found the "on going" card was useful to remind me of tasks about documention and comments.

![trello board](/docs/trello1.jpg)
![trello board](/docs/trello10.jpg)
![trello board](/docs/trello2.jpg)
![trello board](/docs/trello3.jpg)
![trello board](/docs/trello4.jpg)
![trello board](/docs/trello5.jpg)
![trello board](/docs/trello6.jpg)
![trello board](/docs/trello7.jpg)
![trello board](/docs/trello7.jpg)
![trello board](/docs/trello8.jpg)
![trello board](/docs/trello9.jpg)




