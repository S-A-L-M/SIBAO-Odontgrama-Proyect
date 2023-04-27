from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_odontograma = Blueprint("routes_odontograma", __name__)

@routes_odontograma.route('/indexodontograma', methods=['GET'])
def indexodontograma():

    return render_template('/main/ejemploodontograma.html')