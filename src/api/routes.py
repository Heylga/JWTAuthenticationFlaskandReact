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


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm sighnup which sends the saved info to Backend"
    }
    return jsonify(response_body), 200




@api.route('/signup', methods=['GET', 'POST'])
def create_new_user(email, password):

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    print('email', email, 'password', password)

    if email != "test" or password != "test":
        return {"error": "Wrong email or password"}, 400

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response.jsonify({"msg": "user created"}), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  