from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(Form):
    name = StringField("Имя", [validators.DataRequired("Введите имя")])
    email = StringField("Email", [validators.DataRequired("Введите Email"), validators.Email("Неверный Email")])
    subject = StringField("Тема", [validators.DataRequired("Введите текст в поле «Тема»")])
    message = TextAreaField("Сообщение", [validators.DataRequired("Введите текст в поле «Сообщение»")])
    submit = SubmitField("Отправить")

