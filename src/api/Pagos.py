from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Pagos import Pagos, PagosSchema

routes_pagos = Blueprint("routes_pagos", __name__)
#Roles
pago_schema = PagosSchema()
pagos_schema = PagosSchema(many=True)