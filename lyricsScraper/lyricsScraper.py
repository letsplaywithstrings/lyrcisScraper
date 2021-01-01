#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
from bs4 import BeautifulSoup
from itertools import chain
def artist_with_letter(letter):
    if 1 == len(letter):
        r = requests.get("https://genius.com/artists-index/" + letter)
        soup = BeautifulSoup(r.content,"lxml")
        result = soup.find_all("a", attrs= {"class": "artists_index_list-artist_name"})
        resultcon = soup.find_all("li", attrs= {"class": ""})
        resultcon.pop(0)
        resultcon.pop(0)
        resultcon.pop()
        resultcon.pop()
        resultcon.pop()
        final = result + resultcon
        finallist = []
        for item in final:
            finallist.append(item.text.replace("\n", "").replace("\\", "").replace("\u200b" ,"").replace("\u200e",""))
    else:
        print("Please input artists' name's beginning letter.")
    return finallist
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + "3hD_OJ7_zy2oyS1yykZBomVQE2kX7Y3J8K43v0k_1AHQ0aOCnzgUz2oqP24dZxFe"}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response
def request_song_url(artist_name, song_cap):
    page = 1
    songs = {} 
    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower() or hit['result']['primary_artist']['name'].lower() + ",":
                song_info.append(hit)
        if len(song_info) < song_cap:
            song_cap = len(song_info)
        for song in song_info:
            if (len(songs) < song_cap):
                songnames = song['result']['full_title']
                url = song['result']['url']
                songs[songnames.replace("\xa0"," ")] = url
        if (len(songs) == song_cap):
            break
        else:
            page += 1
    return songs
def scrape_song_lyrics(url):
    while True:
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content,"lxml")
            lyrics = soup.find('div', attrs= {"class" : "lyrics"}).text
            break
        except:
            continue
    return lyrics
def scrape_data(firstLetterOfArtist,songCapacityOfEachArtist):
    names = artist_with_letter(firstLetterOfArtist)
    bs = {}
    for name in names:  
        lukes = request_song_url(name, songCapacityOfEachArtist)
        for n,u in lukes.items():
            bs[n] = scrape_song_lyrics(u)
            print(bs)
    return bs
def spesific_lyric(nameOfSongAndArtist):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + "3hD_OJ7_zy2oyS1yykZBomVQE2kX7Y3J8K43v0k_1AHQ0aOCnzgUz2oqP24dZxFe"}
    search_url = (base_url + '/search')
    data = {'q': nameOfSongAndArtist}
    response = requests.get(search_url, data=data, headers=headers)
    json = response.json()
    song_info = []
    spesificlyric = {}
    try:
        song_info.append(json['response']['hits'][0])
        for song in song_info:
            songnames = song['result']['full_title']
            lyric = scrape_song_lyrics(song['result']['url'])
            spesificlyric = songnames.replace("\xa0"," ") + "\n" + lyric
        return spesificlyric
    except:
        print("We have not found lyrics.")
def scrape_artists_songs(artistname,songcapacity):
    songsandurls = request_song_url(artistname, songcapacity)
    wx = {}
    for name,url in songsandurls.items():
        wx[name] = scrape_song_lyrics(url)
    return wx


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




