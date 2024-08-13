#customer forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange
from wtforms import ValidationError
 
# from zcommerce.models import Customer #Add this later when we do the DB stuff
# At present as of 8/12/24, there are no direct interactions with the database, so the above line is commented out, since there is not need in the Customer
# Entry form to interact with the database.
# Later, if I need to do the Update function in the CRUD, I will need to import the Customer model from the models.py file.


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



