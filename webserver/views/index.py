import json
import webserver.models
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, Response

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def index():
    return render_template("index.html")

@index_bp.route("/create/<string:name>", methods=["POST"])
def stats_data(name):
    data = request.get_json()
    s = webserver.models.SystemDao(name=name, data=data)

    pass
