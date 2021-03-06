import json
import os

import redis
from flask import Blueprint, jsonify, request

from confitec.ext.database import Artists, resource
from confitec.services.genius import GeniusAPI

headers = {"Authorization": f"Bearer {os.environ.get('GENIUS_API_KEY')}"}
geniusAPI = GeniusAPI(headers)
artists = Artists(resource)

cache = redis.Redis(host="localhost", port=6379, decode_responses=True)
bp = Blueprint("artists", __name__, url_prefix="/artists/")


@bp.get("/")
def get_artists():
    if not request.args:
        return jsonify({"artists": artists.find_all()})
    artist_name = request.args["q"]
    cache = request.args.get("cache", "").lower()

    if cache == "" or cache == "true":
        cache = True
    else:
        cache = False

    songs = geniusAPI.get_songs(artist_name, cache)
    return jsonify(songs)
