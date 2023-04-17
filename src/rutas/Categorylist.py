from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_categorylist = Blueprint("routes_categorylist", __name__)


@routes_categorylist.route('/indexcategorylist', methods=['GET'] )
def indexcategorylist():
    
    return render_template('/main/Category-list.html')