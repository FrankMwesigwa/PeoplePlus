from flask import Flask, request, jsonify, json
from app.department import departments
from app import db
from app.departments.models import Department, departments_schema, department_schema

# endpoint to create new tasks
@departments.route("/departments", methods=["POST"])
def addDepartment():
    jsn = request.data
    data = json.loads(jsn)

    departmentname = data['departmentname']
    departmentlocation = data['departmentlocation']

    if Department.query.filter_by(departmentname=departmentname).count() == 0:
         department = Department( departmentname,departmentlocation)
        db.session.add(department)
        db.session.commit()

        exists = Department.query.filter_by(departmentname=departmentname)
        if exists.count() > 0:
            return jsonify({'message':'Department has been successfully created'}), 201
        else:
            return jsonify({'message':'Department was not created, please try again'}), 400
    else:
        return jsonify({'message':'Department already exists, please try again'}), 400

# endpoint to get all branch
@department.route("/department", methods=["GET"])
def getAllDepartments():
    if request.method == 'GET':
        branches = Department.query.all()
        result = departments_schema.dump(departments)# deserialize the data picked from the db to json format 
        return jsonify(result.data)
    else:
        return jsonify({"message":'no branch found'}), 400

# endpoint to get branch detail by id
@department.route("/branch/<int:id>", methods=["GET"])
def getdepartmentById(id):
    department = Department.query.get(id)
    if department:
        return department_schema.jsonify(department), 200
    else:
        return jsonify({'message':'no department with that id exists'}), 404

# endpoint to update branch
@department.route("/department/<int:id>", methods=["PUT"])
def updatedepartment(id):
    department = Department.query.get(id)

    department.departmentname = request.json['departmentname']
    department.departmentlocation = request.json['departmentlocation']

    db.session.commit()
    return jsonify({'message':'department successfully updated'}), 201

# endpoint to delete branch
@department.route("/department/<int:id>", methods=["DELETE"])
def deletedepartment(id):
    department = Department.query.get(id)
    
    if department:
        db.session.delete(department)
        db.session.commit()
        return jsonify({'message':'department was deleted successfully'}), 200
    else:
        return jsonify({'message':'no department with that id exists'}), 404



