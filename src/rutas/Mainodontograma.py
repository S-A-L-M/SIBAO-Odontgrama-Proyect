from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_mainodontograma = Blueprint("routes_mainodontograma", __name__)


@routes_mainodontograma.route('/indexmainodontograma', methods=['GET'] )
def indexmainodontograma():
    
    return render_template('/main/MainOdontograma.html')