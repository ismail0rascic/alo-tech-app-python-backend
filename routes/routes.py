
from flask import Blueprint
from controllers.tracks_controller import tracks
from middlewares.tracks_middleware import find_random_artist


api = Blueprint("api", __name__)

@api.before_request
def first_middleware():
    return find_random_artist()

@api.route("/tracks")
def tracks_route():
    return tracks()