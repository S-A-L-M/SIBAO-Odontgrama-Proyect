from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_mainweb = Blueprint("routes_mainweb", __name__)

#---------------------ESTO ES EL LOGIN YA DENTRO DE TEMPLATE ODONTOGRAMA-------------------
@routes_mainweb.route('/indexlogin', methods=['GET'] )
def indexlogin():
    
    return render_template('/main/index.html')
