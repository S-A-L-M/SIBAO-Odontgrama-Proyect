from config.db import db, app, ma 


class Tratamientos(db.Model):
    __tablename__ = "tbltratamientos"


    id  = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    description = db.Column(db.Text)
    duracion = db.Column(db.Date)
    costo = db.Column(db.Double)

    def __init__(self, nombre, description, duracion, costo):
        self.nombre = nombre
        self.description = description
        self.duracion = duracion
        self.costo = costo

with app.app_context():
    db.create_all()

class TratamientosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'description', 'duracion', 'costo')