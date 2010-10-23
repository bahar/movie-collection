from google.appengine.api import urlfetch
import urllib
from BeautifulSoup import BeautifulSoup
import time

def search_movies(title):
  IMDB_URL = 'http://www.imdb.com/find?'
  params = {
    's':'tt',
    'q':title
  }
  result = urlfetch.fetch(url=IMDB_URL+urllib.urlencode(params))
  soup = BeautifulSoup(result.content)
  tables = soup.findAll('table', {'style':None,'class':None})
  response = list()
  for table in tables:
    aas = table.findAll(lambda tag: (tag.img == None) and (tag.name == 'a'))
    for a in aas:
      response.append({'link':a['href'], 'title':a.text})
  return response
