from config.db import db, app, ma 


class Pagos(db.Model):
    __tablename__ = "tblpago"


    id  = db.Column(db.Integer, primary_key=True)
    id_cita = db.Column(db.Integer, db.ForeignKey('tblcitas.id'))
    id_tratamiento = db.Column(db.Integer, db.ForeignKey('tbltratamientos.id'))
    fecha = db.Column(db.DateTime)
    monto = db.Column(db.Double)
    metodo = db.Column(db.String(50))

    def __init__(self, id_cita, id_tratamiento, fecha, monto, metodo):
        self.id_cita = id_cita
        self.id_tratamiento = id_tratamiento
        self.fecha = fecha
        self.monto = monto
        self.metodo = metodo

with app.app_context():
    db.create_all()

class PagosSchema(ma.Schema):
    class Meta:
        fields = ('id','id_cita', 'id_tratamiento', 'fecha, monto', 'metodo')