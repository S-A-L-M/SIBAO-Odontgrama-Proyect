from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_clientsearch = Blueprint("routes_clientsearch", __name__)


@routes_clientsearch.route('/indexclientsearch', methods=['GET'] )
def indexclientsearch():
    
    return render_template('/main/Client-search.html')