import random

from flask import Flask
import flask_restful as restful
import os
import yaml

from flask_cors import CORS, cross_origin


def flask_app_init():
    app = Flask(__name__)
    # resources is needed!
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    return app


FILE_BACK = 'a.yaml'


class HelloWorld(restful.Resource):
    def get(self):
        if os.path.exists(FILE_BACK):
            d = yaml.load(open(FILE_BACK, 'r'))
            print("read successful")
        else:
            d = {'hello': 'world' + str(random.randint(0, 100))}
            print("fresh generate")
            yaml.dump(d, open(FILE_BACK, 'w'))

        return d


def main():
    app = flask_app_init()
    api = restful.Api(app)
    api.add_resource(HelloWorld, '/')

    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 7777)))


if __name__ == '__main__':
    main()
