from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, HiddenField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp

from vshaurme.models import User
from vshaurme.forms.custom_validators import weak_checker


class EditProfileForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired(), Length(1, 30)])
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(1, 20),
                                                   Regexp('^[a-zA-Z0-9]*$',
                                                          message='Имя пользователя может содержать только символы / The username should contain only: a-z, A-Z and 0-9.')])
    website = StringField('Вебсайт', validators=[Optional(), Length(0, 255)])
    location = StringField('Город', validators=[Optional(), Length(0, 50)])
    bio = TextAreaField('Пара слов о себе', validators=[Optional(), Length(0, 120)])
    submit = SubmitField("Редактировать")

    def validate_username(self, field):
        if field.data != current_user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Данное имя пользователя уже используется.')


class UploadAvatarForm(FlaskForm):
    image = FileField('Загрузить', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Файл должен быть в формате .jpg или .png.')
    ])
    submit = SubmitField("Начать загрузку")


class CropAvatarForm(FlaskForm):
    x = HiddenField()
    y = HiddenField()
    w = HiddenField()
    h = HiddenField()
    submit = SubmitField('Обрезать и обновить')


class ChangeEmailForm(FlaskForm):
    email = StringField('Новый адрес почты', validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField("Изменить")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Данный адрес почты уже зарегистрирован.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(
        'Старый пароль',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Новый пароль', 
        validators=[
            DataRequired(), 
            Length(max=128,message="Пароль слишком длиннее 128 символов"), 
            EqualTo('password2'),
            weak_checker
        ]
    )
    password2 = PasswordField(
        'Повторите новый пароль', 
        validators=[DataRequired()]
    )
    submit = SubmitField("Изменить")


class NotificationSettingForm(FlaskForm):
    receive_comment_notification = BooleanField('Новый комментарий')
    receive_follow_notification = BooleanField('Новый подписчик')
    receive_collect_notification = BooleanField('Кто-то взял мое фото себе в коллекцию')
    submit = SubmitField("Принять")


class PrivacySettingForm(FlaskForm):
    public_collections = BooleanField('Мою коллекция видна всем пользователям.')
    submit = SubmitField("Принять")


class DeleteAccountForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField("Удалить")

    def validate_username(self, field):
        if field.data != current_user.username:
            raise ValidationError('Неправильное имя пользователя.')
