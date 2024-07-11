# orders forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired, Email, NumberRange
from wtforms import ValidationError
 


class OrderEntry(FlaskForm):
	customerid = IntegerField('Customer ID: ', validators=[DataRequired()])
	productid = IntegerField('Product ID: ', validators=[DataRequired()])
	orderdate = DateField('Date', validators=[DataRequired()])
	quantity = IntegerField('Quantity', validators=[DataRequired()])
	submit = SubmitField('Enter')
