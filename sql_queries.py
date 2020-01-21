# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays CASCADE; "
user_table_drop = "DROP TABLE IF EXISTS users CASCADE; "
song_table_drop = "DROP TABLE IF EXISTS songs CASCADE; "
artist_table_drop = "DROP TABLE IF EXISTS artists CASCADE; "
time_table_drop = "DROP TABLE IF EXISTS time CASCADE; "

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays( \
    songplay_id SERIAL PRIMARY KEY, \
    start_time bigint REFERENCES time (start_time), \
    user_id smallint REFERENCES users (user_id), \
    level varchar(400) NOT NULL, \
    song_id varchar(400) REFERENCES songs (song_id), \
    artist_id varchar(400) REFERENCES artists (artist_id), \
    session_id int NOT NULL, \
    location varchar(400), \
    user_agent varchar(400)); 
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users( \
    user_id smallint PRIMARY KEY, \
    first_name varchar(40), \
    last_name varchar(40), \
    gender varchar(5), \
    level varchar(10));
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs( \
    song_id varchar(400) PRIMARY KEY, \
    title varchar(400), \
    artist_id varchar(400), \
    year smallint, \
    duration float);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists( \
    artist_id varchar(400) PRIMARY KEY, \
    name varchar(400), \
    location varchar(400), \
    latitude float, \
    longitude float);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time( \
    start_time bigint PRIMARY KEY, \
    hour smallint, \
    day smallint, \
    week smallint, \
    month smallint, \
    year smallint, \
    weekday varchar(10));
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)  DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id)  DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id)  DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)  DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT   s.song_id  ,a.artist_id  FROM songs s  left JOIN artists a  ON s.artist_id = a.artist_id  WHERE s.title = %s  AND a."name" = %s  AND s.duration = %s;
""")

# QUERY LISTS

drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]
create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]