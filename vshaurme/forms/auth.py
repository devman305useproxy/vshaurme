from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

from vshaurme.models import User
from vshaurme.forms.custom_validators import weak_pass_checker


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired(), Length(1, 254), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    name = StringField('Как вас зовут', validators=[DataRequired(), Length(1, 30)])
    email = StringField('Адрес почты', validators=[DataRequired(), Length(1, 254), Email()])
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(1, 20),
                                                   Regexp('^[a-zA-Z0-9]*$',
                                                          message='Имя может содержать символы. The username should contain only a-z, A-Z and 0-9.')])
    password = PasswordField(
        'Пароль', 
        validators=[
            DataRequired(), 
            Length(max=128, message="Пароль слишком длиннее 128 символов"), 
            EqualTo('password2'),
            weak_pass_checker
        ]
    )
    password2 = PasswordField(
        'Повторите пароль', 
        validators=[DataRequired()]
    )
    submit = SubmitField("Зарегистрироваться")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Пользователь с такой почтой уже зарегистрирован. The email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Данное имя пользователя уже используется. The username is already in use.')


class ForgetPasswordForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField("Отправить ссылку для сброса пароля")


class ResetPasswordForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired(), Length(1, 254), Email()])
    password = PasswordField(
        'Пароль', 
        validators=[
            DataRequired(),
            weak_pass_checker, 
            Length(max=128, message="Пароль слишком длиннее 128 символов"),
            EqualTo('password2')
        ]
    )
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField("Далее")
