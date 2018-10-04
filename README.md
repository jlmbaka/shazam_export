# README
Small tool to import and export Shazam playlists. It saves it to a local file and generates a url to convert to to be imported in other applications such as:

* Spotify
* Youtube
* Deezer
* Soundcloud

It uses the API of [PlaylistConverter](http://www.playlist-converter.net) to handle the playlist conversion to the aforementioned Music and video services.

## USAGE
```
> python shazam_playlist.py url
```

## EXAMPLE
python shazam_playlist.py 'https://gist.github.com/jlmbaka/62eb5e8c4bc70300929ec331bc778a53/raw/a719de5766a876ba99267e0b1f0516efece12934/shazam_02102018.html'

## BACKLOG
### Option to save the parse playlist to a specific file
The title is self explainatory

### Parse directly from shazam
So far this utility does not have to ability to directly parse a playlist from [shazam.com](https://shazam.com) it contains account private, account specific information. I go around this limitation by copying the generated html from shazam.com to a publicly accessible url (e.g. [Github's GIST](https://gist.github.com) and query that url instead see [EXEMPLE](#EXEMPLE).