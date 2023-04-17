from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_category = Blueprint("routes_category", __name__)


@routes_category.route('/indexcategory', methods=['GET'] )
def indexcompany():
    
    return render_template('/main/Category.html')