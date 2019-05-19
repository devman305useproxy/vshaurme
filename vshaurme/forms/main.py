from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, Length


class DescriptionForm(FlaskForm):
    description = TextAreaField('Описание', validators=[Optional(), Length(0, 500)])
    submit = SubmitField("Принять")


class TagForm(FlaskForm):
    tag = StringField('Добавьте тег(пробел для разделения)', validators=[Optional(), Length(0, 64)])
    submit = SubmitField("Добавить")


class CommentForm(FlaskForm):
    body = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField("Отправить")
