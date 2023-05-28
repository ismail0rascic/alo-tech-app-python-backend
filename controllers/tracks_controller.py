from flask import  request,  make_response ,jsonify 
from API.spotify import search_tracks


def tracks():
    try:
        artist = request.artist
        response = make_response(search_tracks(artist))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response 
    except Exception as e:
        error_message = make_response("Failed to retrieve tracks", 500)
        error_message.headers['Access-Control-Allow-Origin'] = '*'
        return error_message
          