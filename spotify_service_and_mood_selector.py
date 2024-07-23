import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import json
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI, scope='user-library-read, user-modify-playback-state, user-read-playback-state'))

def get_filtered_songs(mood):
    with open('audio_features.json', 'r') as json_file:
        audio_features = json.load(json_file)

    filtered_songs = []
    for song_features in audio_features:
        if (mood.lower() == 'happy' and song_features['valence'] > 0.5) or \
           (mood.lower() == 'sad' and song_features['valence'] <= 0.5):
            filtered_songs.append(song_features['id'])

    return filtered_songs

def select_song(filtered_songs, mood):
    if filtered_songs:
        selected_song_id = random.choice(filtered_songs)
        uri = sp.track(selected_song_id)['uri']
        sp.start_playback(uris=[uri])

        return True
    return False

def read_track_ids_from_json(filename='saved_track_ids.json'):
    with open(filename, 'r') as json_file:
        track_ids = json.load(json_file)
    return track_ids

def add_random_songs_to_queue(mood, num_songs):
    filtered_songs = get_filtered_songs(mood)
    if filtered_songs:
        for _ in range(min(num_songs, 10)):
            selected_song_id = random.choice(filtered_songs)
            uri = sp.track(selected_song_id)['uri']
            sp.add_to_queue(uri)
            filtered_songs.remove(selected_song_id)
        return True
    return False