from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    search = StringField('ПОИСК', validators=[DataRequired()])
    submit = SubmitField('Найти')