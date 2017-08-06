import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('movie_db.db')

c = conn.cursor()

# let's get the names of our tables
c.execute("select name from sqlite_master where type='table';")
print(c.fetchall())

# We are going to append the other critics tables to our movies table
# First we need to read in all the tables
movies = pd.read_sql('select * from movies', con=conn)
travers = pd.read_sql('select * from travers', con=conn)
morgenstern = pd.read_sql('select * from morgenstern', con=conn)
reed = pd.read_sql('select * from reed', con=conn)
collin = pd.read_sql('select * from collin', con=conn)
lasalle = pd.read_sql('select * from lasalle', con=conn)

# We will create a new column named 'critic' with the critic's name as every value
travers['critic'] = 'travers'
morgenstern['critic'] = 'morgenstern'
reed['critic'] = 'reed'
collin['critic'] = 'collin'
lasalle['critic'] = 'lasalle'

# Drop movies that have not been reviewed
travers = travers.dropna(axis=0, how='any')
morgenstern = morgenstern.dropna(axis=0, how='any')
reed = reed.dropna(axis=0, how='any')
collin = collin.dropna(axis=0, how='any')
lasalle = lasalle.dropna(axis=0, how='any')

# we have an extra index column we do not need
travers = travers.drop(['index'], axis=1)
morgenstern = morgenstern.drop(['index'], axis=1)
reed = reed.drop(['index'], axis=1)
collin = collin.drop(['index'], axis=1)
lasalle = lasalle.drop(['index'], axis=1)

# start appending to create a new table
reviews = travers.append(morgenstern, ignore_index=True)
reviews = reviews.append(reed, ignore_index=True)
reviews = reviews.append(collin, ignore_index=True)
reviews = reviews.append(lasalle, ignore_index=True)

reviews.to_sql('reviews', con=conn)

conn.commit()

conn.close()