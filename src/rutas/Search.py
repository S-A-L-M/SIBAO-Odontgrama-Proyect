from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_search = Blueprint("routes_search", __name__)


@routes_search.route('/indexsearch', methods=['GET'] )
def indexsearch():
    
    return render_template('/main/Search.html')