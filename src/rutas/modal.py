from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_modal = Blueprint("routes_modal", __name__)


@routes_modal.route('/indexmodal', methods=['GET'] )
def indexmainodontograma():
    
    return render_template('/main/modal.html')