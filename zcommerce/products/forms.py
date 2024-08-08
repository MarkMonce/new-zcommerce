#customer forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, DecimalField
from wtforms.validators import DataRequired, Email, NumberRange
from wtforms import ValidationError
 


class ProductEntry(FlaskForm):
	product_name = StringField('Product Name', validators=[DataRequired()])
	product_description = StringField('Description', validators=[DataRequired()])
	product_price = DecimalField('Price', validators=[DataRequired()])
	product_quantity = IntegerField('Quantity in Stock', validators=[DataRequired()])
	submit = SubmitField('Enter')
