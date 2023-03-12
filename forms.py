from wtforms import Form
from wtforms import StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('correo')
    