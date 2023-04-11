from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_login = Blueprint("routes_login", __name__)

@routes_login.route('/indexlogin', methods=['GET'])
def indexlogin():

    return render_template('/main/index.html')