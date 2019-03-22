from app import db,ma
from marshmallow import Schema, fields

class Department(db.Model):
        """
        Create a Department table
        """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    depart_name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    location = db.Column(db.String(120), unique=True)
    user= user = db.Column(db.String(120), unique=True)
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.depart_name)

class DepartmentsSchema(ma.Schema):
    class Meta:
           # Fields to expose
        fields = ('id','depart_name', 'description', 'location', 'user', 'employee')

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many =True)

