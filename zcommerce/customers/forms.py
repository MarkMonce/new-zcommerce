#customer forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange
from wtforms import ValidationError
 
# from zcommerce.models import Customer #Add this later when we do the DB stuff


class CustomerEntry(FlaskForm):
	firstname = StringField('First Name', validators=[DataRequired()])
	lastname = StringField('Last Name', validators=[DataRequired()])
	address1 = StringField('Address 1', validators=[DataRequired()])
	address2 = StringField('Address 2')
	city = StringField('City', validators=[DataRequired()])
	state = StringField('State', validators=[DataRequired()])
	zipcode = StringField('Zip Code', validators=[DataRequired()])
	phone = StringField('Phone', validators=[DataRequired()])
	email = StringField('E-mail Address', validators=[DataRequired()])
	bankbalance = IntegerField('Bank Balance',default=0,validators=[DataRequired(), NumberRange(min=0)])
	submit = SubmitField('Enter')



