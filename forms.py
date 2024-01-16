from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class Contact(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = EmailField(label='Email Address', validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[DataRequired()])
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField('Submit')