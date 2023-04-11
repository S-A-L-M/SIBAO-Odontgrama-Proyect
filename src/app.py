from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#Importar routes API
from api.roles import routes_roles


#rutas
from rutas.odontograma import routes_odontograma

#ubicacion del api
app.register_blueprint(routes_roles, url_prefix="/api")


#ubicacion rutas
app.register_blueprint(routes_odontograma, url_prefix="/fronted")




@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('main/indexLog.html', titles=titulo)


@app.route("/algo")
def otr():
    return "hola mondongo del master-v2"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')