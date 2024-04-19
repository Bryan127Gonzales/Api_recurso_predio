from utils.db import db
from dataclasses import dataclass
'''
@dataclass
class TipoPredio(db.Model):
    id_tipo_predio = db.Column(db.Integer, primary_key=True)
    nombre_predio = db.Column(db.String)
'''
@dataclass
class Predio(db.Model):
    id_predio: int
    id_tipo_predio: int
    descripcion: str
    ruc: str
    telefono: str
    correo: str
    direccion: str
    idubigeo: str
    
    id_predio = db.Column(db.Integer, primary_key=True)
    id_tipo_predio = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    idubigeo = db.Column(db.String(6))

    # Define la relación con la tabla tipo_predio
    #tipo_predio = db.relationship("TipoPredio")

    def __init__(self, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo):
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo