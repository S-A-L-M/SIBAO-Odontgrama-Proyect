from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_mydata = Blueprint("routes_mydata", __name__)


@routes_mydata.route('/indexmydata', methods=['GET'] )
def indexmydata():
    
    return render_template('/main/my-data.html')