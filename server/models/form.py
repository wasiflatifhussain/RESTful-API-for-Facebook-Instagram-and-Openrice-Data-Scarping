from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import url_for

class FB_Link (FlaskForm):
  link = StringField('URL:', validators=[DataRequired()])
  submit = SubmitField('Submit for Facebook Queue')
  # submit = SubmitField('Instagram')
  # submit = SubmitField('Openrice')
  
class IG_Link (FlaskForm):
  link = StringField('URL:', validators=[DataRequired()])
  submit = SubmitField('Submit for Instagram Queue')

class OPR_Link (FlaskForm):
  link = StringField('URL:', validators=[DataRequired()])
  submit = SubmitField('Submit for Openrice Queue')