#!/usr/bin/python3
"""
Flask App
"""

from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ close storage """
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """ note that we set the 404 status explicitly """
    return {"error": "Not found"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
