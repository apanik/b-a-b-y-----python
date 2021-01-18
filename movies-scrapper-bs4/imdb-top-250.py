from bs4 import BeautifulSoup
 
import requests
import sys

index = 1
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text,features='html.parser')
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)
file_ = open("movie-list.txt","w")
for movie in tr:
    title = movie.find('td', {'class': 'titleColumn'} ).find('a').contents[0]
    year = movie.find('td', {'class': 'titleColumn'} ).find('span', {'class': 'secondaryInfo'}).contents[0]
    rating = movie.find('td', {'class': 'ratingColumn imdbRating'} ).find('strong').contents[0]
    row = str(index)+'.' +title + ' - ' + year + ' ' + ' ' + rating + "\n"
    file_.write(row)
    index+=1

file_.close()
