import json
import webserver.models
from flask import Blueprint, request, Response, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route("/api/<string:mbid>/high-level", methods=["GET"])
def get_recommendation(mbid, name):
    """Endpoint for quering recommendation.
    Params:
    mbid: id of the artist or recording used as seed for the recommendation
    name: name of the system to use for recommend.
    """
    #make query to get system data
    try:
        return jsonify(db.data.load_high_level(mbid, offset))
    except NoDataFoundException:
        raise webserver.exceptions.APINotFound("Not found")

@api_bp.route("/api/try-system/", methods=["POST"])
def try_recommendation():
    """Endpoint for quering recommendation, passing a new system.
    Get params:
    mbid: id of the artist or recording used as seed for the recommendation
    data: json with components of the system
    """
    data = request.get_json()

    s = webserver.models.SystemDao(data=data['data'])
    system = s.get_system()
    ret = system.recommend([data['mbid']])
    return Response(json.dumps(ret), content_type='application/json; charset=utf-8')

