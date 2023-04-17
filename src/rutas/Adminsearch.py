from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_adminsearch = Blueprint("routes_adminsearch", __name__)


@routes_adminsearch.route('/indexadminsearch', methods=['GET'] )
def indexadminsearch():
    
    return render_template('/main/Admin-search.html')