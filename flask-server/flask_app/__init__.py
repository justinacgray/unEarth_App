# entry point for our app
from flask import Flask
from .extensions import db, migrate
from .controllers.user_controller import user_controller
import os
from dotenv import load_dotenv
load_dotenv()

db_username = os.getenv('db_username')
db_password = os.getenv('db_pwd')
db_hostname = os.getenv('hostname')
db_portID = os.getenv('port_id')
database = os.getenv('database')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_username}:{db_password}@{db_hostname}:{db_portID}/{database}"
    app.config['SQLALCHEMY TRACK MODIFICATIONS'] = False
    
    
    app.register_blueprint(user_controller, url_prefix='/')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
