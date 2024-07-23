import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI, scope='user-library-read, user-modify-playback-state, user-read-playback-state'))

def get_all_saved_track_ids():
    all_saved_track_ids = []
    offset = 0
    limit = 50 
    while True:
        saved_tracks = sp.current_user_saved_tracks(limit=limit, offset=offset)
        if not saved_tracks['items']:
            break
        for item in saved_tracks['items']:
            track_id = item['track']['id']
            all_saved_track_ids.append(track_id)
        offset += limit
    return all_saved_track_ids

def write_track_ids_to_json(track_ids, filename='saved_track_ids.json'):
    with open(filename, 'w') as json_file:
        json.dump(track_ids, json_file, indent=4)

def main():
    saved_track_ids = get_all_saved_track_ids()
    write_track_ids_to_json(saved_track_ids)

if __name__ == "__main__":
    main()