from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token
from app import app, db
from flask import jsonify, render_template, redirect, request, flash
from app.models.user_model import User
import jwt
import json
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route('/api/user/register', methods=['POST'])
# create user
def register():
    print("inside REGISTER method")
    # what is the difference using brackets vs square braces when using request.form?? 
    # creates a dictionary of the form data
    data = request.form
    # if this is false - that's why we use NOT
    if not User.register_validations(data): 
        return redirect('/')
        
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    favorite_country = data.get('favorite_country')
    print(f"register ===> {first_name}, {last_name}, {email}, {password}, {confirm_password}, {favorite_country}")
    
    # hash_pw = bcrypt.generate_password_hash(password)
    # bcrypt.check_password_hash(hash_pw, password)
    pwhash = bcrypt.generate_password_hash(password).decode('utf-8')
    #password_hash = pwhash.decode('utf8') # decode the hash to prevent is encoded twice
    print("hashed password ===> ", pwhash)
    
    # inserts user
    new_user = User(
    first_name = first_name,
    last_name=last_name,
    email=email,
    password=pwhash,
    favorite_country=favorite_country
    )
    # insert into database
    db.session.add(new_user)
    db.session.commit()
    flash("Account created!", category='success')
        
    print("new_user ===>", new_user)
    
    access_token = create_access_token(identity=new_user.id)
    print("access_TOKEN===>", access_token)
    return jsonify(access_token=access_token)
    
    
@app.route("/")
def home():
    return "home page"

@app.route("/dashboard")
def dashboard():
    return "dashboard"

@app.route('/api/user/login', methods=["POST"])
def login():
    print("inside LOGIN")
    data = request.form
    
    email = data.get('email')
    password = data.get('password')
    print("EMAIL & PASSWORD ====>", email, password)
    user =  User.query\
        .filter_by(email = email)\
        .first()
    if not User.login_validations(data): 
        return redirect('/')
    

    if user:
        if not bcrypt.check_password_hash(user.password, password):
            flash("Sorry, these credentials are invalid. Please, try again", category='error')
            print("something went wrong with password")
            
        else:
            flash("Successfully logged in", category='success')
            access_token = create_access_token(identity=user.id)
            print("access_TOKEN===>", access_token)
            print("SUCCESS!!!")
            return jsonify(access_token=access_token)
    else:
        flash("Email does not exist", category='error')
        print("email doesn't exist")
        
    return redirect("/dashboard")


@app.route('/api/user/logout')
def logout(request):
    request.session.flush() #todo change this to clear token?
    return redirect("/") 


# get all users
@app.route("/api/users", methods=['GET'])
def get_all_users():
    users = User.query.order_by(User.id.asc()).all()
    user_list = []
    for user in users:
        user_list.append(User.format_user(user))
    return {"users ": user_list}

# get 1 user
@app.route('/api/users/<id>/', methods=['GET'])
def get_one_user(id):
    user = User.query.filter_by(id=id).one()
    formatted_user = User.format_user(user)
    return {"formatted_user" : formatted_user}


@app.route("/api/users/delete/<id>", methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).one()
    db.session.delete(user)
    db.session.commit()
    return f"User (id: {id}) Deleted"

@app.route("/api/users/update/<id>", methods=['PUT'])
def update_user(id):
    
    data = request.form
    user = User.query.filter_by(id=id)
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    favorite_country = data.get('favorite_country')
    
    user.update(dict(first_name=first_name, last_name=last_name, email=email, favorite_country=favorite_country, updated_at=datetime.utcnow()))
    db.session.commit()
    return {'user' : User.format_user(user.one())}





print("inside user controllers")
