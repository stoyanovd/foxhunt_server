from flask import Flask
import flask_restful as restful
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
