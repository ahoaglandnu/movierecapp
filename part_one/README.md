# Part One: Collecting the 2017 Movies

### Overview

Here we are going to create a csv file of the released and to-be released 2017 movies. We will pull this information from Wikipedia.
https://en.wikipedia.org/wiki/2017_in_film

### Setup

#### Launch your virtual environment. 

I used Anaconda and Python 3.6.1. To check your version from the command line, type:

`$ python -V*`

Activate virtual environment:

`$ source activate <name_of_environment>` 

If you have not created a virtual environment before, you can read more here:
https://conda.io/docs/using/envs.html

More on conda vs. pip vs. virtualenv
https://conda.io/docs/_downloads/conda-pip-virtualenv-translator.html

### Collecting 2017 Movie Titles

Packages used:

*Requests*
*BeautifulSoup*
*Pandas*

`$ pip -r requirements.txt`

#### To collect movie titles:

`$ python movietitles.py`

### Collecting Movie Reviews


We need a list of movie critics. Metacritic is a great starting point. Unfortunately, we cannot scrape their website and the API has been down since the CBS acquisition.

#### Manual creation of csv files:

To get the database started, I manually looked up the 2017 reviews of five of the most popular critics according to metacritic. Next, I opened the _movies2017.csv_ file and manually added a "liked" column and added a 1 for a positive review and 0 for a negative review.

#### Make a sqlite database:

Next, we run the *makeadb.py* file in the same directory as the csv files. This will create 'movies.db'

`$ python makeadb.py`

I used sqlite for now since this is a small project.

#### Launch sqlite3 to ensure the table was created:

`$ sqlite3 movie_db.db`

`sqlite> .tables`

`sqlite> .schema`

`sqlite> select * from movies where movie_id = 0;`

You should see:

`0|0|Underworld: Blood Wars`

`sqlite> .exit`

