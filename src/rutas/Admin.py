from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_admin = Blueprint("routes_admin", __name__)


@routes_admin.route('/indexadmin', methods=['GET'] )
def indexadmin():
    
    return render_template('/main/Admin.html')