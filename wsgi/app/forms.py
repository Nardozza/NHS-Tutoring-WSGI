from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_wtf import Form
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from app.models import User


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default = False)

    def validate_password(self):
        try:
            user = User.query.filter(User.username == self.username.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not user.is_valid_password(self.password.data):
            raise ValidationError("Invalid password")



class RegistrationForm(Form):
    username = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    password = StringField(validators=[DataRequired])

    def check_email_uniqueness(self, field):
        user = User.query.filter(User.email == field.data).first()
        if user is not None:
            raise ValidationError("A user with that email already exists")

