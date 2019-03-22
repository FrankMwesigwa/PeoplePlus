from app import db,ma
from marshmallow import Schema, fields

class Department(db.Model):
	    
	__tablename__ = 'departments'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	location = db.Column(db.String(200))
 
    def __init__(self, name, location):
        self.name = name,
        self.location = location

        
class DepartmentSchema(ma.Schema):
    class Meta:
        fields = ('id','name','location')

department_schema = DepartmentSchema()
departments_schema = DepartmenSchema(many =True)