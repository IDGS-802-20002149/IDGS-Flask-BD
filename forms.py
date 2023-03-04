from wtforms import Form
from wtforms import StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = StringField('id', [validators.DataRequired(message='Hola')])
    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('correo')
    