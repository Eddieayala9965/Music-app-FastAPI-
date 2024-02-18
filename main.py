from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import session
from models import Artist, Song, Playlist

app = FastAPI()

@app.get('/artist')
def get_artist():
    artists = session.query(Artist)
    return artists.all()

@app.get('/song')
def get_song():
    songs = session.query(Song)
    return songs.all()

@app.get('/playlist')
def get_playlist():
    playlists = session.query(Playlist, Artist, Song).join(Artist, Artist.id == Playlist.artist_id).join(Song, Song.id == Playlist.song_id)
    results = playlists.all()
    playlist_list = []
    for playlist  in results:
        playlist_dict = {
            "id": playlist.Playlist.id,
            "artist_id": playlist.Artist.name,
            "song_id": playlist.Song.name
        }
        playlist_list.append(playlist_dict)
    return playlist_list

@app.post('/add/artist')
async def add_artist(name: str):
    new_artist = Artist(name=name)
    session.add(new_artist)
    session.commit()
    return {'artist added': new_artist.name}

@app.post('/add.song')
async def add_song(name: str):
    new_song = Song(name=name)
    session.add(new_song)
    session.commit()
    return {'song added': new_song.name}

@app.post('/add/playlist')
async def add_playlist(name: str, artist_id: int, song_id: int):
    new_playlist = Playlist(name = name, artist_id = artist_id, song_id = song_id)
    session.add(new_playlist)
    session.commit()
    return {'playlist added': new_playlist} 


