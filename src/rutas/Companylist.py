from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_companylist = Blueprint("routes_companylist", __name__)


@routes_companylist.route('/indexcompanylist', methods=['GET'] )
def indexcompany():
    
    return render_template('/main/Company-list.html')