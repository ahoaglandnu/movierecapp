from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

# homepage
@app.route('/')
def index():
	return render_template('index.html')

# Movies
@app.route('/films')
def films():
	conn = sql.connect('movie_db.db')
	c = conn.cursor()
	c.execute("select movies, count(*) from reviews group by movies order by count(*) desc;")
	rows = c.fetchall();
	return render_template('films.html', rows=rows)

# Single Movie
@app.route('/film/<string:movies>')
def film(movies):
	conn = sql.connect('movie_db.db')
	c = conn.cursor()
	c.execute("select critic from reviews where liked=1 and movies = ? ;", [movies])
	likes = c.fetchall();
	c.execute("select critic from reviews where liked=0 and movies= ? ;", [movies])
	dislikes = c.fetchall();
	return render_template('film.html', likes=likes, dislikes=dislikes, movies=movies)


if __name__ == '__main__':
	app.run(debug=True)