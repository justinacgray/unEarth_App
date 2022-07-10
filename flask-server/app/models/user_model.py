from ..config.postgres_connection import connectToPostgres
import datetime
import re
from app import db, app
from flask import flash
from sqlalchemy import func
from uuid import uuid4
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)


# https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy
#CRUD will be

def get_uuid():
    return uuid4().hex

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    first_name = db.Column(db.String(255), nullable=False) #can't be empty field, MUST have a value
    last_name = db.Column(db.String(255), nullable=False)
    email= db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    favorite_country  = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    # one to many relationship
    # saved_searches = db.relationship('Search') #has to be capital- do not why but it must
    
    def __init__(self, first_name, last_name, email, password, favorite_country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.favorite_country = favorite_country
        # self.created_at = created_at
        # self.updated_at = updated_at
        
    def __repr__(self):
        # https://stackoverflow.com/questions/1984162/purpose-of-repr-method
        print("\n THIS IS WHAT THE __repr__ METHOD DOES!!!")
        return f"NEW USER ====>: {self.first_name, self.last_name, self.email, self.favorite_country}"
    
    @staticmethod
    def register_validations(data):
        is_valid = True
        print("data===>" , data)
        
        # current_user =  User.query.filter_by(email=data['email']).first()
        # print("current user===>", current_user)
    
        # #email already in use
        # Todo - fix this validation
        # if current_user:
        #     flash("That email is already in use", category='error')
        #     is_valid = False
        # data needs to be wrapped in parenthesis in order for it to be read
        if len(data("first_name")) < 2:
            flash( "First Name must be at least 2 characters", category='error')
            is_valid = False
            
        #length of the last name
        if len(data("last_name")) < 2:
            flash("Last Name ust be at least 2 characters", category='error')
            is_valid = False
            
        
        if len(data('email')) == 0:
            flash("Email must be entered")
            is_valid = False
            
        #email matches format
        if not EMAIL_REGEX.match(data('email')):    # test whether a field matches the pattern            
            flash("invalid email address!", category='error')
            is_valid = False
            
        #password was entered was less than 8
        if len(data('password')) < 8:
            flash("Password must be minimum 8 characters", category='error')
            is_valid = False
            
        if (data('password') != data('confirm_password')):
            flash("Passwords do not match", category='error')
            is_valid = False
        print("completed validations")
        return is_valid


    @staticmethod
    def login_validations(data):
        is_valid = True
        
        if len(data['email']) == 0:
            flash("Email must be entered", category='error')
            is_valid = False
            
        if len(data['password']) == 0:
            flash("Password must be entered", category='error')
            is_valid = False
            
            
    
print("inside user model")