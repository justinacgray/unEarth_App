from flask import Blueprint, render_template, redirect, request
from ..extensions import db
from flask_app.models.user_model import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/')
def home():
    return "<h1>Shalom!</h1>"

