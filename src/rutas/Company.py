from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_company = Blueprint("routes_company", __name__)


@routes_company.route('/indexcompany', methods=['GET'] )
def indexcompany():
    
    return render_template('/main/Company.html')