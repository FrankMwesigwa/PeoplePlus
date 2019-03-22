from app import db,ma
from marshmallow import Schema, fields

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(200))
    username = db.column(db.String(20))
    email = db.Column(db.String(60), unique=True)
    contact = db.column(db.String(14))

    def __init__(self, firstname,lastname,username,email,contact):
        self.firstname = firstname
        self.lastname = lastname,
        self.username = username,
        self.email  = email ,
        self.contact = contact

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','firstname','lastname','username','email','contact')

user_schema = UserSchema()
users_schema = UserSchema(many =True)