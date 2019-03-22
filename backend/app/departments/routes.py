from flask import Flask, request, jsonify, json
from app.getAllDepartments import department
from app import db
from app.department.model import Department, departments_schema, department_schema


@department.route("/department", methods=["POST"])
def addDepartment():
    jsn = request.data
    data = json.loads(jsn)

    name = data['name']
    location = data['location']
    
    if Department.query.filter_by(name=name).count() == 0:
        department = Department(name,location)
        db.session.add(department)
        db.session.commit()

        exists = Department.query.filter_by(name=name)
        if exists.count() > 0:
            return jsonify({'message':'Department has been successfully created'}), 201
        else:
            return jsonify({'message':'Department was not created, please try again'}), 400
    else:
        return jsonify({'message':'Department already exists, please try again'}), 400

# endpoint to get all department
@department.route("/department", methods=["GET"])
def getAllDepartments():
    if request.method == 'GET':
        departments = Department.query.all()
        result = departments_schema.dump(departments)# deserialize the data picked from the db to json format 
        return jsonify(result.data)
    else:
        return jsonify({"message":'no department found'}), 400

# endpoint to get department detail by id
@department.route("/department/<int:id>", methods=["GET"])
def getdepartmentById(id):
    department = Department.query.get(id)
    if department:
        return department_schema.jsonify(department), 200
    else:
        return jsonify({'message':'no department with that id exists'}), 404

# endpoint to update department
@department.route("/department/<int:id>", methods=["PUT"])
def updatedepartment(id):
    department = Department.query.get(id)

    department.name = request.json['name']
    department.location = request.json['location']

    db.session.commit()
    return jsonify({'message':'department successfully updated'}), 201

# endpoint to delete department
@department.route("/department/<int:id>", methods=["DELETE"])
def deletedepartment(id):
    department = Department.query.get(id)
    
    if department:
        db.session.delete(department)
        db.session.commit()
        return jsonify({'message':'department was deleted successfully'}), 200
    else:
        return jsonify({'message':'no department with that id exists'}), 404