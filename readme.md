# Playlist Api Web Server

In PostgreSQL use the following commands to create the database playlist_api and the user list_dev. list_dev will be granted pivileges to work on the database.

```psql
CREATE DATABASE playlist_api;
CREATE USER list_dev WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE playlist_api TO list_dev;
GRANT ALL ON SCHEMA public to list_dev;

```




## R1 

## R3 Why have you chosen this database system. What are the drawbacks compared to others?

---

PostgreSQL is a powerful open-source relational database system. PostgreSQL offers cutting-edge functionality and dependability. It is robust and stable. PostgreSQL also has a reputation for being highly reliable with a strong focus on consistency and data integrity. Features like ACID(Atomicity, Consistency, Isolation, Durability) properties help ensure the integrity of data. PostgreSQL is designed to handle large amounts of data and high levels of traffic loads. Because it supports scalability features such has table partitioning, replication & clustering it makes it suitable for growing web applications. PostgreSQL has efficient handling of JSON documents in the database. A great advantage is the large and active community of users and developers, leading to large amounts of resources, documentation and support of the community. 

For all the great advantages there are also some disadvantages, such has the learning curve and configuration options. This can be overwhelming at times. Additional work is needed for proper configuration to achieve optimal performance. 
PostgreSQL has a memory management that can be demanding when dealing with larger datasets.

CREATE DATABASE playlist_api;
CREATE USER list_dev WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE playlist_api TO list_dev;
GRANT ALL ON SCHEMA public to list_dev;
