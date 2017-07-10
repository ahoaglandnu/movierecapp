# Quick script to build a sqlite db.
import sqlite3
import pandas as pd 

# Our csv files as dataframes
movies = pd.read_csv('movies2017.csv')
travers = pd.read_csv('travers2017.csv')
morgenstern = pd.read_csv('morgenstern2017.csv')
reed = pd.read_csv('reed2017.csv')
collin = pd.read_csv('collin2017.csv')
lasalle = pd.read_csv('lasalle2017.csv')

movie_db = 'movie_db.db'

conn = sqlite3.connect(movie_db)

c = conn.cursor()

# our dataframes to SQL tables
movies.to_sql('movies', con = conn)
travers.to_sql('travers', con = conn)
morgenstern.to_sql('morgenstern', con = conn)
reed.to_sql('reed', con = conn)
collin.to_sql('collin', con = conn)
lasalle.to_sql('lasalle', con = conn)

conn.commit()

conn.close()