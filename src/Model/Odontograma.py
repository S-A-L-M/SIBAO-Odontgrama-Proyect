from config.db import db, app, ma 


class Odontograma(db.Model):
    __tablename__ = "tblodontograma"


    id  = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    fecha_consulta = db.Column(db.Date)
    odontologo = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    description = db.Column(db.Text)
    tratamiento_recomendado = db.Column(db.String(50))
    fecha_creacion = db.Column(db.Date)

    def __init__(self, id_paciente, fecha_consulta, odontologo, description, tratamiento_recomendado, fecha_creacion):
        self.id_paciente = id_paciente
        self.fecha_consulta = fecha_consulta
        self.odontologo = odontologo
        self.description = description
        self.tratamiento_recomendado = tratamiento_recomendado
        self.fecha_creacion = fecha_creacion

with app.app_context():
    db.create_all()

class OdontogramaSchema(ma.Schema):
    class Meta:
        fields = ('id','id_paciente', 'fecha_consulta', 'odontologo', 'description', 'tratamiento_recomendado', 'fecha_creacion')