from config.db import db, app, ma 


class Historial(db.Model):
    __tablename__ = "tblhistorial"


    id  = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    diagnostico = db.Column(db.String(50))
    tratamiento = db.Column(db.String(50))
    medicamentos = db.Column(db.String(50))
    fecha_creacion = db.Column(db.Date)

    def __init__(self, id_paciente, diagnostico, tratamiento, medicamentos, fecha_creacion):
        self.id_paciente = id_paciente
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.medicamentos = medicamentos
        self.fecha_creacion = fecha_creacion

with app.app_context():
    db.create_all()

class HistorialSchema(ma.Schema):
    class Meta:
        fields = ('id','id_paciente', 'diagnostico', 'tratamiento', 'medicamentos','fecha_creacion')