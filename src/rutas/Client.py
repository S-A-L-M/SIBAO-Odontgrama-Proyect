from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_client = Blueprint("routes_client", __name__)


@routes_client.route('/indexclient', methods=['GET'] )
def indexclient():
    
    return render_template('/main/Client.html')