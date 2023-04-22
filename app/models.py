# app/models.py

from app import db
import datetime

class Alimento(db.Model):
    """
    Create a Alimentos table
    """

    __tablename__ = 'alimento'

    codigo = db.Column(db.String(10), primary_key=True)
    tipo = db.Column(db.String(20))
    categoria = db.Column(db.String(20))
    proveedor = db.Column(db.String(50))
    descripcion = db.Column(db.String(200))
    kg = db.Column(db.String(8))
    precio = db.Column(db.String(8))
    ean = db.Column(db.String(13))
    arriba = db.Column(db.Integer())
    abajo = db.Column(db.Integer())

class Venta(db.Model):
    """
    Create a Alimentos table
    """

    __tablename__ = 'venta'
    id = db.Column(db.Integer(), primary_key=True)
    codigo = db.Column(db.String(10))
    tipo = db.Column(db.String(20))
    categoria = db.Column(db.String(20))
    proveedor = db.Column(db.String(50))
    descripcion = db.Column(db.String(200))
    kg = db.Column(db.String(8))
    precio = db.Column(db.Float())
    ean = db.Column(db.String(13))
    fecha =db.Column(db.DateTime(),default=datetime.datetime.utcnow)
