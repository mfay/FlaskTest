from wtforms.csrf.session import SessionCSRF
from datetime import timedelta
from wtforms import Form, StringField, validators
from flask import session

class MyBaseForm(Form):
    class Meta:
      csrf = True
      csrf_class = SessionCSRF
      csrf_secret = b'EPj00jpf23903.,adsklasasdfklxwBBSQfnQ9DJYe0Ym'
      csrf_time_limit = timedelta(minutes=20)

      @property
      def csrf_context(self):
        return session

class RegistrationForm(MyBaseForm):
  firstName = StringField('First Name', [validators.Length(min=1, max=255)])
  lastName = StringField('Last Name', [validators.Length(min=1, max=255)])
  email = StringField('Email', [validators.Length(min=4, max=255)])