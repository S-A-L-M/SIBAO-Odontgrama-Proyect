from config.db import db, app, ma 


class Usuarios(db.Model):
    __tablename__ = "tblusuarios"


    id  = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    rol = db.Column(db.Integer, db.ForeignKey('tblrolesusuarios.id'))
    fecha_nacimiento = db.Column(db.Date)
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String(50))
    fecha_creacion = db.Column(db.Date)
    fecha_actualizacion = db.Column(db.Date)

    def __init__(self, nombre, rol, fecha_nacimiento, direccion, telefono, correo, fecha_creacion, fecha_actualizacion):
        self.nombre = nombre
        self.rol = rol
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion

with app.app_context():
    db.create_all()

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'rol', 'fecha_nacimiento', 'direccion', 'telefono', 'correo', 'fecha_creacion', 'fecha_actualizacion')