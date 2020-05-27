from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

from models import Users, UserById


app = Flask(__name__)
api = Api(app)

#
# Endpoints
#

# Quotes
api.add_resource(Users, '/quotes') 
api.add_resource(UserById, '/quotes/<id>') 

# Tags
api.add_resource(Users, '/tags') 
api.add_resource(UserById, '/tags/<id>') 

# Authors
api.add_resource(Users, '/authors') 
api.add_resource(UserById, '/authors/<id>') 

if __name__ == '__main__':
    app.run()