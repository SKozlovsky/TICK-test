from flask import Flask
from flask_restful import Resource, Api
import os
import signal

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self):
        return {'Status': 'OK', 'AppName': 'TICK-test'}


class Shutdown(Resource):
    def get(self):
        print("Killing flask process ...")
        os.kill(1, signal.SIGTERM)


api.add_resource(Index, '/')
api.add_resource(Shutdown, '/stop')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')