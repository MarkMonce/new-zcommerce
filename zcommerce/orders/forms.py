# orders forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired, Email, NumberRange
from wtforms import ValidationError
 


class OrderEntry(FlaskForm):
	customer_id = IntegerField('Customer ID: ', validators=[DataRequired()])
	product_id = IntegerField('Product ID: ', validators=[DataRequired()])
	order_date = DateField('Date', validators=[DataRequired()])
	order_quantity = IntegerField('Quantity', validators=[DataRequired()])
	submit = SubmitField('Enter')
