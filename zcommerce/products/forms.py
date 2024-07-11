#customer forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, NumberRange
from wtforms import ValidationError
 


class ProductEntry(FlaskForm):
	product_name = StringField('Product Name', validators=[DataRequired()])
	product_description = StringField('Description', validators=[DataRequired()])
	product_price = FloatField('Price', validators=[DataRequired()])
	product_quantity = IntegerField('Quantity in Stock', validators=[DataRequired()])
	submit = SubmitField('Enter')
