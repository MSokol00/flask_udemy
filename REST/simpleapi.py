from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_migrate import Migrate
import os

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'mysecretkey'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)
Migrate(APP, DB)

API = Api(APP)
JWT = JWT(APP, authenticate, identity)


##########
class Puppy(DB.Model):
    name = DB.Column(DB.String(80), primary_key=True)
    
    def __init__(self, name):
        self.name = name
        
    def json(self):
        return {'name': self.name}
##############

class PuppyNames(Resource):
    """PuppyClass"""

    def get(self, name):
        """get method"""
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()
        return {'name': None}, 404

    def post(self, name):
        """post method"""
        pup = Puppy(name=name)
        DB.session.add(pup)
        DB.session.commit()
        return pup.json()

    def delete(self, name):
        """delete method"""
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            DB.session.delete(pup)
            DB.session.commit()
            return {'note': 'delete success'}
        return {'name': None}, 404


class AllNames(Resource):
    """AllNames"""

    #@jwt_required()
    def get(self):
        """get method"""
        puppies = Puppy.query.all()
        
        return [pup.json() for pup in puppies]

API.add_resource(PuppyNames, '/puppy/<string:name>')
API.add_resource(AllNames, '/puppies')


if __name__ == '__main__':
    APP.run(debug=True)
