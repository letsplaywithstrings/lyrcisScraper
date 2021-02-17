# lyrcisScraper
You can scrape song lyrics that you want.
## Getting Started
You can get lyrics easily with this small module. Also, you can get all artists whose name begins with specific letter with this module.Furthermore this module can get all song lyrics of artists whose name begins with a specific letter.
## Prerequisites and Installing
You need to install this module with the following code below from pypi.
```
pip install lyricsScraper
```
## Usage

**First of all, you must import this module to your py projects by the following code below.**
```phyton
from lyricsScraper import lyricsScraper
```

-------------------------------------------------------------------------

If you want to get all artists whose name begins with a specific letter, use the following function below.
```phyton
artist_with_letter(letter)
```
This function will return list of artists.

-------------------------------------------------------------------------

If you want to get artist's songs, use the following function below.
```phyton
request_song_url(artist_name, song_cap)
```
This function will return a dictionary of songnames and genius song urls.

-------------------------------------------------------------------------

If you want to scrape song lyrics with genius song url, use that following function below.
```phyton
scrape_song_lyrics(url)
```
It will return as a string.

-------------------------------------------------------------------------

If you want to scrape all song lyrics whose artist name begins with a specific letter, use the following function below.You must define the song capacity of each artist.
```phyton
scrape_data(firstLetterOfArtist,songCapacityOfEachArtist)
```
It will return a dictionary.

-------------------------------------------------------------------------

If you want to get song lyrics with song name and artist, use the following function below. You can probably get lyrics by defining only song name.
```phyton
spesific_lyric(nameOfSongAndArtist)
```
It will return a string

-------------------------------------------------------------------------

If you want to get song lyrics of a spesific artist, use the following function below.You must define the song capacity.
```phyton
scrape_artists_songs(artistname,songcapacity)
```
It will return a dictionary.

-------------------------------------------------------------------------
-------------------------------------------------------------------------

## Bulit With
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

# License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/letsplaywithstrings/lyrcisScraper/blob/main/LICENSE) file for details
