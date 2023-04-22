from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Historial import Historial, HistorialSchema

routes_hostorial = Blueprint("routes_historial", __name__)
#Roles
historial_schema = HistorialSchema()
historiales_schema = HistorialSchema(many=True)