# lyrcisScraper
You can scrape song lyrics that you want.
## Getting Started
You can get lyrics easily with this small module.Also, you can get all artists whose name begins with specific letter with this module.Furthermore this module can get all song lyrics of artists whose name is begin with spesific letter.
## Prerequisites and Installing
You need install requests and BeautifulSoup, You can install with following codes below.
```
pip install BeautifulSoup
pip install requests
```
Also you can run setup.py. It will install prerequisites.
## Usage
If you want get all artists whose name is begin with spesific letter.
```phyton
artist_with_letter(letter)
```
This function will return list of artists.

-------------------------------------------------------------------------

If you want get artist's songs. Use the following function below.
```phyton
request_song_url(artist_name, song_cap)
```
This function will return dictionary of songnames and genius song urls.

-------------------------------------------------------------------------

If you want scrape song lyrics with genius song url. Use that following function below.
```phyton
scrape_song_lyrics(url)
```
It will return as a string.

-------------------------------------------------------------------------

If you want scrape all song lyrics whose artist name is begin with spesific letter.You must define song capacity of each artist. Use that following function below.
```phyton
scrape_data(firstLetterOfArtist,songCapacityOfEachArtist)
```
It will return a dictionary.

-------------------------------------------------------------------------

If you want get song lyrics with song name and artist, you use that following function below.In addition,You can probably get lyrics by defining only song name.
```phyton
spesific_lyric(nameOfSongAndArtist)
```
It will return a string

-------------------------------------------------------------------------
-------------------------------------------------------------------------

## Bulit With
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

# License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/letsplaywithstrings/lyrcisScraper/blob/main/LICENSE) file for details
