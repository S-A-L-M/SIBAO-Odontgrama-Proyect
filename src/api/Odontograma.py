from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Odontograma import Odontograma, OdontogramaSchema

routes_odontograma = Blueprint("routes_odontograma", __name__)
#Roles
odontograma_schema = OdontogramaSchema()
odontogramas_schema = OdontogramaSchema(many=True)