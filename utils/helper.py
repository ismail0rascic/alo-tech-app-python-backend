import random
from data.data import data
from collections import OrderedDict


def formatTracks (results):
    tracks_list = []
    sorted_results = sorted(results['tracks']['items'], key=lambda x: x['popularity'], reverse=True)
    
    top_tracks = sorted_results[:10]
    
    for track in top_tracks:
        track_info = {
            'artist': track['artists'][0]['name'],
            'track': track['name'],
            'album_image_url': track['album']['images'][0]['url'],
            'preview_url': track['preview_url']
        }
        tracks_list.append(track_info)
    
    return tracks_list

def randomArtist(q):
    return random.choice(data[q])
