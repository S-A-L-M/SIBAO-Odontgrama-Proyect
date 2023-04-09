from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#Importar routes
from api.roles import routes_roles
from rutas.Mainweb import routes_mainweb

#rutas
from rutas.Mainweb import routes_mainweb
from rutas.login import routes_login

#ubicacion del api
app.register_blueprint(routes_roles, url_prefix="/api")


#ubicacion rutas
app.register_blueprint(routes_login, url_prefix="/fronted")


@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/main/MainOdont.html', titles=titulo)


@app.route("/algo")
def otr():
    return "hola Santiago"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')