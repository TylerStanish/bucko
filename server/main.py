import traceback

from flask import Flask, g, jsonify
from marshmallow import ValidationError
import psycopg2.extras
from psycopg2.pool import ThreadedConnectionPool

from auth.routes import auth_blueprint
from utils.db import get_db_info



def create_app():
    app = Flask(__name__)

    db_info = get_db_info()
    pool = ThreadedConnectionPool(0, 16, **db_info, cursor_factory=psycopg2.extras.RealDictCursor)

    @app.before_request
    def before_request():
        g.db = pool.getconn()

    @app.after_request
    def after(res):
        pool.putconn(g.db)
        return res

    # register blueprints
    app.register_blueprint(auth_blueprint)

    # error handling
    @app.errorhandler(ValidationError)
    def handle_invalid_request_data(e: ValidationError):
        return jsonify(e.messages), 400

    # TODO add in a catch-all error handler?
    @app.errorhandler(Exception)
    def catchall(e: Exception):
        # traceback.print_exc(e)
        # TODO please format exceptions and print, don't propagate them
        raise e
        return jsonify({'error': 'There was an internal server error'}), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

