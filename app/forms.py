from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
from app.models import Player

# form to submit new player to database
class PlayerForm(Form):
	nickname = StringField('user nickname', validators = [DataRequired()])
	main = StringField('main', validators = [DataRequired()])
	ranking = IntegerField('ranking', validators = [NumberRange(min = 0, max = 500)])
	description = StringField('player description', validators = [Length(min = 0, max = 500)])
