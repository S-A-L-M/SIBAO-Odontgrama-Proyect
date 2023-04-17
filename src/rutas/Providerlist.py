from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_providerlist = Blueprint("routes_providerlist", __name__)


@routes_providerlist.route('/indexproviderlist', methods=['GET'] )
def indexproviderlist():
    
    return render_template('/main/Provider-list.html')