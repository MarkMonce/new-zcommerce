#customer forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, NumberRange
from wtforms import ValidationError
 


class ProductEntry(FlaskForm):
	productname = StringField('Product Name', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	price = FloatField('Price', validators=[DataRequired()])
	stockqty = IntegerField('Quantity in Stock', validators=[DataRequired()])
	submit = SubmitField('Enter')
