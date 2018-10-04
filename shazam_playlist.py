from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import csv
import sys

def configSoup(url):
  # specify the url
  shazam_page = url
  # query the website and return the html
  page = urlopen(shazam_page)
  # parse html using soup
  soup = BeautifulSoup(page, 'html.parser')
  return soup

def getSongs(soup):
  # get title
  title_tags = soup.find_all('div', attrs={ 'class': 'title' })
  titles = [title_tag.a.text.strip() for title_tag in title_tags]
  print(len(title_tags))
  # get artist
  artist_tags = soup.find_all('div', attrs={ 'class': 'artist' })
  artists = [artist_tag.a.text.strip() if artist_tag.a is not None else artist_tag.div.text.strip() for artist_tag in artist_tags]

  # zip artist and title
  songs = [(title, artist) for title, artist in zip(titles, artists)]
  return songs

def format_tracks(tracks):
  return ['%s - %s' % track for track in tracks]

def save_to_csv(songs, filename, format=True):
  with open(filename, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for song in set(songs):
      row = None
      if format:
        row = [song[0], song[1]]
      else:
        print(song)
        row = [('{0} - {1}' % song).strip()]
      writer.writerow(row)

def generate_trackconverter_url(songs):
  tracks = format_tracks(songs)
  tracks_joined = '\n'.join(tracks)
  url = 'http://www.playlist-converter.net/#/freetext=' + quote(tracks_joined);
  return url

if __name__ == "__main__":
  url = len(sys.argv) > 1 and sys.argv[1]
  if (url):
    soup = configSoup(url)
    songs = getSongs(soup)
    save_to_csv(songs, filename='songs_formated.csv')
    url = generate_trackconverter_url(songs)
    print('Follow this url:')
    print(url);
  else:
    print('usage: shazam_playlist.py url')