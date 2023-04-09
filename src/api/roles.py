from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.RolesUsuario import RolesUsuarios, RolesSchema

routes_roles = Blueprint("routes_rol", __name__)
#Roles
rolesusuario_schema = RolesSchema()
rolesusuarios_schema = RolesSchema(many=True)

@routes_roles.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Hola Mundo!!"


#Roles
#---------SAVE/CREAR------------
@routes_roles.route('/saveroles', methods=['POST'] )
def guardar_roles():
    #request.form['title']
    roles = request.json['roles']
    print(roles)
    new_rol = RolesUsuarios(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/rusuarios')


@routes_roles.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = RolesUsuarios.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(rolesusuario_schema.dump(rol)) 

@routes_roles.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = RolesUsuarios.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/rusuarios')
