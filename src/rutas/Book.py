from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_book = Blueprint("routes_book", __name__)


@routes_book.route('/indexbook', methods=['GET'] )
def indexbook():
    
    return render_template('/main/Book.html')