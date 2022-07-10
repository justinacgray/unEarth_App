from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token
from app import app, db
from flask import jsonify, render_template, redirect, request, flash
from app.models.user_model import User
import jwt
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route('/register/user/', methods=['GET','POST'])
# create user
def register():
    print("inside REGISTER method")
    # what is the difference using brackets vs square braces when using request.form?? 
    data = request.form.get
    # shouldn't this be NOT
    if User.register_validations(data): 
        return redirect('/')
        
    first_name = data('first_name')
    last_name = data('last_name')
    email = data('email')
    password = data('password')
    confirm_password = data('confirm_password')
    favorite_country = data('favorite_country')
    print(f"register ===> {first_name}, {last_name}, {email}, {password}, {confirm_password}, {favorite_country}")
    
    hash_pw = bcrypt.generate_password_hash(password)
    bcrypt.check_password_hash(hash_pw, password)
    print("hashed password ===> ", hash_pw)
    
    new_user = User(
    first_name = first_name,
    last_name=last_name,
    email=email,
    password=hash_pw,
    favorite_country=favorite_country
    )
    # insert into database
    db.session.add(new_user)
    db.session.commit()
    flash("Account created!", category='success')
        
    print("new_user ===>", new_user)
    
    access_token = create_access_token(identity=email)
    print("access_TOKEN===>", access_token)
    return jsonify(access_token=access_token)
    
    
@app.route("/")
def home():
    return "hi"

@app.route('/login', methods=["GET", "POST"])
def login():
    data = request.form.get
    if request.method == 'POST':
        email = data['email']
        password = data['password']
        
        if len(email) == 0:
            flash("Email must be entered", category='error')
        if len(password) == 0:
            flash("Password must be entered", category='error')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                flash("Successfully logged in", category='success')
                request.session['user_id'] = user.id
            else:
                flash("Sorry, these credentials are invalid. Please, try again", category='error')
        else:
            flash("Email does not exist", category='error')
    return render_template('login') #todo => change render??


@app.route('/logout')
def logout(request):
    request.session.flush()
    return redirect("/")


# get all users
@app.route("/all_users", methods=['GET'])
def get_all_users():
    all_users = User.query.order_by(User.id.asc()).all()
    user_list = []
    for user in all_users:
        user_list.append(user)
    return user_list

# get 1 user
@app.route('/users/<id>/', methods=['GET'])
def get_one_user(id):
    user = User.query.filter_by(id=id).one()
    return user


@app.route("/users/<id>update", methods=['PUT'])
def update_user(id):
    pass

@app.route("/users/<id>/delete", methods=['DELETE'])
def delete_user(id):
    pass



# todo - get user in session?
# @app.route('/dashboard')
# def dashboard(request):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     one_user = User.objects.filter(id=request.session['user_id'])
#     context = {
#         'user': one_user[0]
#     }

#     return render_template(request, 'success.html', context)



print("inside user controllers")
