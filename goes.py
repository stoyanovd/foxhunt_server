import random

from flask import Flask
import flask_restful as restful
import os

from flask_cors import CORS, cross_origin


def flask_app_init():
    app = Flask(__name__)
    # resources is needed!
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    return app


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world' + str(random.randint(0, 100))}


def main():
    app = flask_app_init()
    api = restful.Api(app)
    api.add_resource(HelloWorld, '/')

    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 7777)))


if __name__ == '__main__':
    main()
