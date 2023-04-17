from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_provider = Blueprint("routes_provider", __name__)

@routes_provider.route('/indexprovider', methods=['GET'])
def indexprovider():

    return render_template('/main/Provider.html')