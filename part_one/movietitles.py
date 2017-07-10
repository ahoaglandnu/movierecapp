from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get('https://en.wikipedia.org/wiki/2017_in_film').text

soup = BeautifulSoup(r, 'html.parser')

rows = []
for table in soup.findAll('table', {'class': 'wikitable'}):
    for row in table.findAll('tr')[1:]:
        cells = []
        for cell in row.findAll('i'):
            cells.append(cell.text)
        rows.append(cells)

del rows[:34]

clean_rows = [l[0] for l in rows]

movie_id = range(0,218)

df = pd.DataFrame({'movie_id': movie_id,'movies': clean_rows})

df.to_csv('movies2017.csv', index=False)