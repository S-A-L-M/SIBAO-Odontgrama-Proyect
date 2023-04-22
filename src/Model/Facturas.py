from config.db import db, app, ma 


class Facturas(db.Model):
    __tablename__ = "tblfacturas"


    id  = db.Column(db.Integer, primary_key=True)
    id_pago = db.Column(db.Integer, db.ForeignKey('tblpago.id'))
    id_paciente = db.Column(db.Integer)
    id_tratamiento = db.Column(db.Integer)
    fecha = db.Column(db.DataTime)
    total = db.Column(db.Double)

    def __init__(self, id_pago, id_paciente, id_tratamiento, fecha, total):
        self.id_pago = id_pago
        self.id_paciente = id_paciente
        self.id_tratamiento = id_tratamiento
        self.fecha = fecha
        self.total = total

with app.app_context():
    db.create_all()

class FacturasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_pago', 'id_paciente', 'id_tratamiento', 'fecha', 'total')