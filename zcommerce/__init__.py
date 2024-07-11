##zcommerce/__init__.py

#CORE ORGANIZATIONAL STRUCTURE FOR OVERALL APP
#Blueprints
#CONFIGS
# more

from flask import Flask
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'zimplepimpledimple'
csrf = CSRFProtect(app)

from zcommerce.core.views import core
from zcommerce.error_pages.handlers import error_pages
from zcommerce.customers.views import customers
from zcommerce.products.views import products
from zcommerce.orders.views import orders

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(customers)
app.register_blueprint(products)
app.register_blueprint(orders)


