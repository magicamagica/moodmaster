import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def read_track_ids_from_json(filename='saved_track_ids.json'):
    with open(filename, 'r') as json_file:
        track_ids = json.load(json_file)
    return track_ids

def get_audio_features(track_ids):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))
    audio_features = []
    for i in range(0, len(track_ids), 100):
        track_ids_batch = track_ids[i:i+100]
        features_batch = sp.audio_features(tracks=track_ids_batch)
        audio_features.extend(features_batch)
    return audio_features

def write_audio_features_to_json(audio_features, filename='audio_features.json'):
    with open(filename, 'w') as json_file:
        json.dump(audio_features, json_file, indent=4)

def main():
    track_ids = read_track_ids_from_json()
    audio_features = get_audio_features(track_ids)
    write_audio_features_to_json(audio_features)

if __name__ == "__main__":
    main()