"""
Very simple Flask web site, with one page
displaying a course schedule.

"""

import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging


# Our own module
# import acp_limits


###
# Globals
###
app = flask.Flask(__name__)
import CONFIG
import uuid
from poi import POI

app.secret_key = str(uuid.uuid4())
app.debug=CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)

poilist=POI(CONFIG.poi).getData()

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
  app.logger.debug("Main page entry")
  flask.session.clear()
  flask.g.pois = poilist
  flask.g.mapquestk= CONFIG.mapquestKey
  flask.g.mapboxk= CONFIG.mapboxKey
  return flask.render_template('map.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("index")
    return flask.render_template('page_not_found.html'), 404



if __name__ == "__main__":
    app.secret_key = str(uuid.uuid4())
    app.debug=CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

