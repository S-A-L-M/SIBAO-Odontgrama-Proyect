from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Facturas import Facturas, FacturasSchema

routes_facturas = Blueprint("routes_facturas", __name__)
#Roles
factura_schema = FacturasSchema()
facturas_schema = FacturasSchema(many=True)