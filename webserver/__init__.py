from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging, sys

import sys
import os

app = Flask(__name__, static_url_path="/static", static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

logging.basicConfig(stream=sys.stderr)

# Configuration
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
import config
app.config.from_object(config)

# Template utilities
app.jinja_env.add_extension('jinja2.ext.do')
app.context_processor(lambda: dict(get_static_path="static"))

from webserver.views.api import api_bp
app.register_blueprint(api_bp)
from webserver.views.stats import stats_bp
app.register_blueprint(stats_bp)
from webserver.views.index import index_bp
app.register_blueprint(index_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)
