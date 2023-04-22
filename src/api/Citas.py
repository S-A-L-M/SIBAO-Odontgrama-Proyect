from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Citas import Citas, CitasSchema

routes_citas = Blueprint("routes_citas", __name__)
#Roles
cita_schema = CitasSchema()
citas_schema = CitasSchema(many=True)