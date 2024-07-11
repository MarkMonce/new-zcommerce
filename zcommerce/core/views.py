# core/views.py
##Core flask views (routes) for the base page(s)

from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
	return render_template('index.html')

# for some apps, may include an "info" route to an info page

