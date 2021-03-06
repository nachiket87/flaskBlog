from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label="Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sign up')


class LoginForm(FlaskForm):
    email = StringField(label="Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField(label='Login')
