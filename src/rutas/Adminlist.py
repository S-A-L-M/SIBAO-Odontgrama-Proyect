from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_adminlist = Blueprint("routes_adminlist", __name__)


@routes_adminlist.route('/indexadminlist', methods=['GET'] )
def indexadminlist():
    
    return render_template('/main/Admin-list.html')