from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Usuarios import Usuarios, UsuariosSchema

routes_user = Blueprint("routes_user", __name__)
#Roles
user_schema = UsuariosSchema()
users_schema = UsuariosSchema(many=True)