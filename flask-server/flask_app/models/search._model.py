from flask_app.config.postgres_connection #from flask_app => config => postgres_connection
from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from  flask_cors import CORS
from flask_app import app


class Search:
    pass