from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_clientlist = Blueprint("routes_clientlist", __name__)


@routes_clientlist.route('/indexclientlist', methods=['GET'] )
def indexclientlist():
    
    return render_template('/main/Client-list.html')