from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class UsernameForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=1, max=10)])
    submit = SubmitField('good username')