from flask import Flask
from flask_restful import Resource, Api
import os
import signal
from time import sleep



app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class shutdown(Resource):
    def get(self):
        print("shutdown")
        os.kill(1, signal.SIGTERM)
        return {'goodby': 'worssssld'}

api.add_resource(HelloWorld, '/')
api.add_resource(shutdown, '/stop')


if __name__ == '__main__':
    sleep(30)
    app.run(debug=True, host='0.0.0.0')