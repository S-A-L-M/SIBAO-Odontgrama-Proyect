from config.db import db, app, ma 


class Citas(db.Model):
    __tablename__ = "tblcitas"


    id  = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer,db.ForeignKey('tblusuarios.id'))
    id_odontoloo = db.Column(db.Integer,db.ForeignKey('tblusuarios.id'))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    nota = db.Column(db.Text)

    def __init__(self, id_paciente, id_odontoloo, fecha, hora, nota):
        self.id_paciente = id_paciente
        self.id_odontoloo = id_odontoloo
        self.fecha = fecha
        self.hora = hora
        self.nota = nota

with app.app_context():
    db.create_all()

class CitasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_paciente', 'id_odontoloo', 'fecha', 'hora', 'nota')