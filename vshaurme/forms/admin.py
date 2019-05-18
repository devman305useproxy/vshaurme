from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email

from vshaurme.forms.user import EditProfileForm
from vshaurme.models import User, Role


class EditProfileAdminForm(EditProfileForm):
    email = StringField('Почта', validators=[DataRequired(), Length(1, 254), Email()])
    role = SelectField('Роль', coerce=int)
    active = BooleanField('Активен. Active')
    confirmed = BooleanField('Подтвержден. Confirmed')
    submit = SubmitField("Принять")

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Данное имя пользователя уже используется.The username is already in use.')

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Данный адрес почты уже зарегистрирован. The email is already in use.')
