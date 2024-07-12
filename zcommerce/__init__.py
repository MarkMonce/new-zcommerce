##zcommerce/__init__.py

#CORE ORGANIZATIONAL STRUCTURE FOR OVERALL APP
#Blueprints
#CONFIGS
# more
import os
from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


##########################################
# DATABASE SETUP
##########################################




app = Flask(__name__)
app.config['SECRET_KEY'] = 'zimplepimpledimple'
basedirectory = os.path.abspath(os.path.dirname(__file__))  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedirectory, 'zcommercedb.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


csrf = CSRFProtect(app) #I dont think I'm using this right now
db = SQLAlchemy(app)
Migrate(app, db)


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


