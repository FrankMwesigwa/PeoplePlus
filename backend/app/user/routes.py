from flask import Flask, request, jsonify, json
from app.user import user
from app import db
from app.user.model import User, users_schema, user_schema


@user.route("/user", methods=["POST"])
def addUser():
    jsn = request.data
    data = json.loads(jsn)

    lastname = data['firstname']
    lastname = data['lastname']
    username = data['username']
    email = data['email']
    contact = data['contact']

    if user.query.filter_by(name=name).count() == 0:
        user = User(lastname,lastname,username,email,contact)
        db.session.add(user)
        db.session.commit()

        exists = User.query.filter_by(name=name)
        if exists.count() > 0:
            return jsonify({'message':'User has been successfully created'}), 201
        else:
            return jsonify({'message':'User was not created, please try again'}), 400
    else:
        return jsonify({'message':'User already exists, please try again'}), 400


@user.route("/user", methods=["GET"])
def getAllUsers():
    if request.method == 'GET':
       users = User.query.all()
       result = users_schema.dump(users)
       return jsonify(result.data)
    else:
        return jsonify({"message":'no user found'}), 400


@user.route("/user/<int:id>", methods=["GET"])
def getuserById(id):
    user = User.query.get(id)
    if user:
        return user_schema.jsonify(user), 200
    else:
        return jsonify({'message':'no user with that id exists'}), 404


@user.route("/user/<int:id>", methods=["PUT"])
def edituser(id):
    user= User.query.get(id)

    user.firstname = request.json['firstname']
    user.lastname = request.json['lastname']
    user.username = request.json['username']
    user.email = request.json['email']
    user.contact = request.json['contact']

    db.session.commit()
    return jsonify({'message':'user successfully updated'}), 201


@user.route("/user/<int:id>", methods=["DELETE"])
def deleteuser(id):
    user = User.query.get(id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message':'user was deleted successfully'}), 200
    else:
        return jsonify({'message':'no user with that id exists'}), 404