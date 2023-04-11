from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.RolesUsuario import RolesUsuarios
routes_loginandregister = Blueprint("routes_loginandregister", __name__)

@routes_loginandregister.route('/indexloginandregister', methods=['GET'])
def indexloginandregister():

    return render_template('/main/indexLog.html')