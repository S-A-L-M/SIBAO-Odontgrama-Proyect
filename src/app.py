from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#Importar routes API
from api.roles import routes_roles


#rutas | ¡¡¡RECUERDA PRIMERO IMPORTAR LA RUTA Y DESPUÉS AGREGARLO EN LA UBICACION DE RUTAS!!!! |
from rutas.odontograma import routes_odontograma
from rutas.home import routes_home
from rutas.Company import routes_company
from rutas.Companylist import routes_companylist
from rutas.Category import routes_category
from rutas.Categorylist import routes_categorylist
from rutas.Provider import routes_provider
from rutas.Providerlist import routes_providerlist
from rutas.Book import routes_book
from rutas.Admin import routes_admin
from rutas.Adminlist import routes_adminlist
from rutas.Adminsearch import routes_adminsearch
from rutas.Client import routes_client
from rutas.Login import routes_login
from rutas.Mainodontograma import routes_mainodontograma
from rutas.Clientsearch import routes_clientsearch
from rutas.Catalog import routes_catalogo
from rutas.Clientlist import routes_clientlist

#ubicacion del api
app.register_blueprint(routes_roles, url_prefix="/api")


#ubicacion rutas
app.register_blueprint(routes_odontograma, url_prefix="/fronted")
app.register_blueprint(routes_home, url_prefix="/fronted")
app.register_blueprint(routes_company, url_prefix="/fronted")
app.register_blueprint(routes_companylist, url_prefix="/fronted")
app.register_blueprint(routes_category, url_prefix="/fronted")
app.register_blueprint(routes_categorylist, url_prefix="/fronted")
app.register_blueprint(routes_provider, url_prefix="/fronted")
app.register_blueprint(routes_providerlist, url_prefix="/fronted")
app.register_blueprint(routes_book, url_prefix="/fronted")
app.register_blueprint(routes_admin, url_prefix="/fronted")
app.register_blueprint(routes_adminlist, url_prefix="/fronted")
app.register_blueprint(routes_adminsearch, url_prefix="/fronted")
app.register_blueprint(routes_client, url_prefix="/fronted")
app.register_blueprint(routes_login, url_prefix="/fronted")
app.register_blueprint(routes_mainodontograma, url_prefix="/fronted")
app.register_blueprint(routes_clientsearch, url_prefix="/fronted")
app.register_blueprint(routes_catalogo, url_prefix="/fronted")
app.register_blueprint(routes_clientlist, url_prefix="/fronted")






@app.route("/")
def index():
    titulo= "Pagina Principal"
    return render_template('main/MainOdontograma.html', titles=titulo)


@app.route("/algo")
def otr():
    return "hola mondongo del master-v2"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')