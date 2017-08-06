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
	c.close()
	return render_template('films.html', rows=rows)

# Single Movie
@app.route('/film/<string:movies>')
def film(movies):
	conn = sql.connect('movie_db.db')
	c = conn.cursor()
	c.execute("select critic from reviews where liked=1 and movies = ? ;", [movies])
	likes = c.fetchall();
	c.execute("select critic from reviews where liked=0 and movies = ? ;", [movies])
	dislikes = c.fetchall();
	c.execute("select count(*) from reviews where liked=1 and movies = ? ;", [movies])
	numLikes = c.fetchone();
	c.execute("select count(*) from reviews where liked=0 and movies = ? ;", [movies])
	numDislikes = c.fetchone();
	c.close()
	return render_template('film.html', likes=likes, dislikes=dislikes, movies=movies, numDislikes=numDislikes, numLikes=numLikes)

# Critics
@app.route('/critics')
def critics():
	conn = sql.connect('movie_db.db')
	c = conn.cursor()
	c.execute("select critic, count(*) from reviews group by critic order by count(*) desc;")
	rows = c.fetchall()
	c.close()
	return render_template('critics.html', rows=rows)

# Single Critic
@app.route('/critic/<string:critic>')
def review(critic):
	conn = sql.connect('movie_db.db')
	c = conn.cursor()
	c.execute("select movies from reviews where liked=1 and critic = ? ;", [critic])
	likes = c.fetchall();
	c.execute("select movies from reviews where liked=0 and critic = ? ;", [critic])
	dislikes = c.fetchall();
	c.execute("select count(*) from reviews where liked=1 and critic = ? ;", [critic])
	numLikes = c.fetchone();
	c.execute("select count(*) from reviews where liked=0 and critic = ? ;", [critic])
	numDislikes = c.fetchone();
	c.close()
	return render_template('critic.html', likes=likes, dislikes=dislikes, critic=critic, numDislikes=numDislikes, numLikes=numLikes)


if __name__ == '__main__':
	app.run(debug=True)