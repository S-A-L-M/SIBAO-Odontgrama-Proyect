from config.db import db, app, ma 


class RolesUsuarios(db.Model):
    __tablename__ = "tblrolesusuarios"


    id  = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(50))

    def __init__(self, roles):
        self.roles = roles

with app.app_context():
    db.create_all()

class RolesSchema(ma.Schema):
    class Meta:
        fields = ('id','roles')