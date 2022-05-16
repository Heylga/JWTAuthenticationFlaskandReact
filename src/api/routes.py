"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm sighnup which sends the saved info to Backend"
    }
    return jsonify(response_body), 200


@api.route('/signup', methods=['POST'])
def create_new_user(email, password):

    body = request.get_json()
    if body is None:
        return {"error": "The body is null or undefined"}, 400
     
    User.create_user(body['email'], body['password'])
    return jsonify({"msg": "user created"}), 200



@api.route('/signup', methods=['POST'])
def create_new_user(email, password):

    body = request.get_json()
    if body is None:
        return {"error": "The body is null or undefined"}, 400
     
    User.create_user(body['email'], body['password'])
    return jsonify({"msg": "user created"}), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)