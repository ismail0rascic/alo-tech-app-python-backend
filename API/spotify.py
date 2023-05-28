import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from config.config import client_id, client_secret

from utils.helper import formatTracks

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_tracks(artist,limit=50):
    results = sp.search(q=f'artist:"{artist}"', type='track', limit=limit)
    return formatTracks(results)