from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_catalog = Blueprint("routes_catalog", __name__)


@routes_catalog.route('/indexcatalog', methods=['GET'] )
def indexcatalog():
    
    return render_template('/main/Catalog.html')