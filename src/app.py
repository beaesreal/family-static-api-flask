"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


# Create the jackson family object
jackson_family = FamilyStructure("Jackson")
member1 = { "id" : jackson_family._generateId(),
            "firstname" :"John", 
            "lastname": jackson_family.last_name,
            "age" : 33, 
            "luckyNumbers": [7, 13, 22]}
member2 = { "id" : jackson_family._generateId(),
            "firstname" :"Jane", 
            "lastname": jackson_family.last_name,
            "age" : 35, 
            "luckyNumbers": [10, 14, 3]}
member3 = { "id" : jackson_family._generateId(),
            "firstname" :"Jimmy", 
            "lastname": jackson_family.last_name,
            "age" : 5, 
            "luckyNumbers": [1]}
jackson_family.add_member(member1)
jackson_family.add_member(member2)
jackson_family.add_member(member3)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Get all members

@app.route('/members', methods=['GET'])
def handle_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }

    return jsonify(response_body), 200


# Get one member by its ID

@app.route('/member/<int:member_id>', methods=['GET'])
def handle_member(member_id):
    member = jackson_family.get_member(member_id)

    if "msg" in member : return jsonify(member), 400

    return jsonify(member), 200


# Post new member

@app.route('/member', methods=['POST'])
def add_member():
    member = request.get_json()

    if member["age"] <= 0: return jsonify({"msg":"Age must be over 0"}), 400

    jackson_family.add_member(member)
    return jsonify(member), 200


# Delete one member by its ID

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.delete_member(member_id)

    if "msg" in member : return jsonify(member), 400

    member["done"] = True
    return jsonify(member), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
