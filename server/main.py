import logging
import traceback

from flask import Flask, g, jsonify
from flask_cors import CORS
from marshmallow import ValidationError
import psycopg2.extras
from psycopg2.pool import ThreadedConnectionPool
from werkzeug.exceptions import HTTPException

from auth.exceptions import ApiException
from auth.routes import auth_blueprint
from utils.db import get_db_info



def create_app():
    app = Flask(__name__)
    CORS(app)
    app.url_map.strict_slashes = False

    db_info = get_db_info()
    pool = ThreadedConnectionPool(0, 16, **db_info, cursor_factory=psycopg2.extras.NamedTupleCursor)

    @app.before_request
    def before_request():
        g.db = pool.getconn()

    @app.after_request
    def after(res):
        from flask import request
        pool.putconn(g.db)
        return res

    # register blueprints
    app.register_blueprint(auth_blueprint)

    logging.basicConfig(filename='error.log', level=logging.DEBUG)

    # error handling
    @app.errorhandler(ValidationError)
    def handle_invalid_request_data(e: ValidationError):
        return jsonify(e.messages), 400

    # TODO add in a catch-all error handler?
    @app.errorhandler(ApiException)
    def catchall(e: ApiException):
        return jsonify({'error': e.message}), e.status_code

    # TODO add in a catch-all error handler?
    @app.errorhandler(Exception)
    def catchall(e: Exception):
        # TODO please format exceptions and print, don't propagate them
        print(traceback.format_exc())
        app.logger.error(e)
        code = 500
        msg = 'There was an internal server error'
        if isinstance(e, HTTPException):
            code = e.code
            msg = str(e)
        return jsonify({'error': msg}), code

    return app


