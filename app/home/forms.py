# Forms for admin blueprint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,FloatField
from wtforms.validators import DataRequired


class AlimentoForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    codigo = StringField('Codigo', validators=[DataRequired()])
    tipo = StringField('Tipo', validators=[DataRequired()])
    categoria = StringField('Categoria')
    proveedor = StringField('Proveedor', validators=[DataRequired()])
    descripcion = StringField('Descripcion', validators=[DataRequired()])
    kg = StringField('Peso')
    precio = FloatField('Precio')
    ean = StringField('ean')
    arriba = IntegerField('Local')
    abajo = IntegerField('Deposito')
    submit = SubmitField('Submit')

class EanForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    ean = StringField('EAN', validators=[DataRequired()])
    producto = StringField('Description')
    codigo = StringField('Codigo')
    submit = SubmitField('Submit')
