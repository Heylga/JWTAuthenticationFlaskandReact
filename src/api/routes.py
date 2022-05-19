"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""

import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = Blueprint('api', __name__)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token) 


@api.route('/hello', methods=['GET'])
@jwt_required() 
def get_hello():

    email = get_jwt_identity()
    dictionary = {
        "message": "hello world"
    }

    return jsonify(dictionary), 200



@api.route('/login', methods=['GET', 'POST'])
def login_user(email, password):

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    print('email', email, 'password', password)

    if email != "test" or password != "test":
        return {"error": "Wrong email or password"}, 400

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response.jsonify({"msg": "user created"}), 200




@api.route('/signup', methods=['POST'])
def register_user(email, password):

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    #Now we need to create a list of information which should be passed to the DataBase
    #We dont need to mention ID here, because its set up automatically
    our_user = User (

        email = email,
        password = password,
        is_active = False,

    )

    #save the user (from models.py)
    our_user.save_user()
    
    return jsonify(our_user.serialize())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  