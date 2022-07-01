# from ..extensions import db
# from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy


# # https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy

# class Search(db.Model):
#     __tablename__ = 'searches'
#     id = db.Column(db.Integer, primary_key=True)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     # one to many relationship
#     user_id = db.Column(db.Integer, db.models.ForeignKey("user.id", verbose_name=(""), on_delete=models.CASCADE)) #sql loweracases the Class User and referring to its id hence why it's user.id
    
    
#     def __init__(self):
#         pass
        
#     def __repr__(self):
#         # https://stackoverflow.com/questions/1984162/purpose-of-repr-method
#         print("THIS IS WHAT THE __repr__ METHOD DOES!!!")
#         return f"Event: {}"