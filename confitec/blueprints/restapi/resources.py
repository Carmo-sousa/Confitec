from flask import jsonify
from flask_restful import Resource


class ArtistResource(Resource):
    def get(self):  # TODO: Implementar esse método!
        musics = ["Lana", "Matanza"]
        return jsonify({"musics": musics})
