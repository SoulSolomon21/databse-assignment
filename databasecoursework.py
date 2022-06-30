import csv
from cs50 import SQL

open("dbcourse.db", "w").close()

db  = SQL("sqlite:///dbcourse.db")

db.execute("""CREATE TABLE movies(
    m_id INTEGER PRIMARY KEY,
    Title TEXT
)""")

db.execute("""CREATE TABLE genres(
    g_id INTEGER PRIMARY KEY,
    Genre TEXT
)""")

db.execute("""CREATE TABLE movie_genres(
    movie_genre_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES movies(m_id),
    FOREIGN KEY (genre_id) REFERENCES genres(g_id)
)""")

with open("gross movies.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["Film"].strip().capitalize()
        db.execute("""INSERT INTO movies(Title) VALUES(?)""", title)

        genre = row["Genre"].strip().capitalize()
        db.execute("""INSERT INTO genres(Genre) VALUES(?)""", genre)
        
        db.execute("INSERT INTO movie_genres(movie_id,genre_id)  VALUES((SELECT m_id FROM movies WHERE Title = ?),(SELECT g_id FROM genres WHERE Genre = ?))", title,genre)


