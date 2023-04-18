from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_myaccount = Blueprint("routes_myaccount", __name__)


@routes_myaccount.route('/indexmyaccount', methods=['GET'] )
def indexmydata():
    
    return render_template('/main/My-account.html')