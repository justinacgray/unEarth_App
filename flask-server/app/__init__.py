# entry point for our app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()
app = Flask(__name__)
db = SQLAlchemy()
jwt = JWTManager(app)


db_username = os.getenv('db_username')
db_password = os.getenv('db_pwd')
db_hostname = os.getenv('hostname')
db_portID = os.getenv('port_id')
database = os.getenv('database')
jwt_secret = os.getenv('JWT_SECRET')
flask_secret = os.getenv('FLASK_SECRET')

app.config['SQLALCHEMY_DATABASE_URI']= f"postgresql://{db_username}:{db_password}@{db_hostname}:{db_portID}/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = flask_secret


# app.register_blueprint(user_controller, url_prefix='/')

migrate = Migrate()
migrate.init_app(app, db)
db.init_app(app)









# app.register_blueprint(user_controller, url_prefix='/')





print("inside init")