import pandas as pd
import sqlalchemy as db
from sqlalchemy import text
import pandas as pd
import json

with open('config.json') as file:
    config = json.load(file)


engine = db.create_engine(f"mysql://root:root@{config['database']['host']}:{config['database']['port']}/db_movies_netflix_transact")
conn = engine.connect()

query = """
SELECT 
    movie.movieID as movieID, movie.movieTitle as title, movie.releaseDate as releaseDate, 
    gender.name as gender , person.name as participantName, participant.participantRole as roleparticipant 
FROM movie 
INNER JOIN participant 
ON movie.movieID=participant.movieID
INNER JOIN person
ON person.personID = participant.personID
INNER JOIN movie_gender 
ON movie.movieID = movie_gender.movieID
INNER JOIN gender 
ON movie_gender.genderID = gender.genderID
"""

movies_data=pd.read_sql(query, con=conn) 
movies_data["movieID"]=movies_data["movieID"].astype('int')
print(movies_data)