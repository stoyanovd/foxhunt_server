from flask import Flask
import flask_restful as restful
import os

from flask_cors import CORS, cross_origin

app = Flask(__name__)
# cors = CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
api = restful.Api(app)


# @app.route("/")
# @cross_origin()
# def helloWorld():
#   return {'hello': 'world'}

class HelloWorld(restful.Resource):
    # @cross_origin()
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
