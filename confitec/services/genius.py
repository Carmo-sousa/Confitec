import json

import redis
import requests

from confitec.ext.database import Artists, resource

cache = redis.Redis(host="redishost", port=6379, decode_responses=True)


class GeniusAPI:
    def __init__(self, headers):
        self.headers = headers
        self.BASE_API = "https://api.genius.com/search"

    def get_songs(self, artist_name, in_cache=True):
        artists = Artists(resource)

        if in_cache:
            songs = cache.get(artist_name.replace(" ", "-"))
            if not songs:
                print("Hello", flush=True)
                response = requests.get(
                    f"{self.BASE_API}",
                    params={"q": artist_name},
                    headers=self.headers,
                ).json()
                return response["response"]
            return json.loads(songs)

        response = requests.get(
            f"{self.BASE_API}",
            params={"q": artist_name},
            headers=self.headers,
        ).json()

        if response["meta"]["status"] == 200:
            if not artists.find_one(artist_name):
                artists.save(artist_name)
                cache.set(
                    artist_name.replace(" ", "-"), json.dumps(response["response"])
                )

            return response["response"]
