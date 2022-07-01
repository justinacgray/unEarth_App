import datetime
from sqlalchemy import func
from app import db
# https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False) #can't be empty field, MUST have a value
    last_name = db.Column(db.String(255), nullable=False)
    email= db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    favorite_country  = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    # one to many relationship
    # saved_searches = db.relationship('Search') #has to be capital- do not why but it must
    
    
    def __init__(self, first_name, last_name, email, password, created_at, updated_at):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        
    def __repr__(self):
        # https://stackoverflow.com/questions/1984162/purpose-of-repr-method
        print("THIS IS WHAT THE __repr__ METHOD DOES!!!")
        return f"Event: {self.first_name, self.last_name, self.email, self.created_at, self.updated_at}"
    
    
print("inside user model")