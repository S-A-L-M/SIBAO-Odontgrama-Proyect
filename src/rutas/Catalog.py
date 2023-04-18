from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_catalogo = Blueprint("routes_catalogo", __name__)


@routes_catalogo.route('/indexcatalogo', methods=['GET'] )
def indexcatalogo():
    
    return render_template('/main/Catalog.html')