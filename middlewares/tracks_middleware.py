from flask import  request, make_response
from utils.validation import  validate_genre_input
from data.data import data
from utils.helper import randomArtist

def find_random_artist():
    q=request.args.get('q')
    error = validate_genre_input(data, q)

    if error:
       error= make_response(error,400)
       error.headers['Access-Control-Allow-Origin'] = '*'  
       return error 
    else:
        request.artist = randomArtist(q)
        return None