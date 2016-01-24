import json
import webserver.models
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, Response

stats_bp = Blueprint('stats', __name__, static_folder='static')

@stats_bp.route("/stats")
def stats():
    return render_template("stats/stats.html")

@stats_bp.route("/stats/<string:name>", methods=["POST"])
def stats_data(name):
    data = request.get_json()
    s = webserver.models.SystemDao(data=data)
    system = s.get_system()

    return Response(json.dumps(system.get_graphs()),
        content_type='application/json; charset=utf-8')

