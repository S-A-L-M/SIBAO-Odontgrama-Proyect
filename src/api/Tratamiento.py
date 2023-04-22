from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.tratamientos import Tratamientos, TratamientosSchema

routes_tratamientos = Blueprint("routes_tratamientos", __name__)
#Roles
tratamiento_schema = TratamientosSchema()
tratamientos_schema = TratamientosSchema(many=True)