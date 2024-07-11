#views.py
#Product views.py
from flask import render_template,url_for,redirect,request,Blueprint
###ADD DB STUFF LATER
from zcommerce import db
from zcommerce.models import Product
from zcommerce.products.forms import ProductEntry

### DO NOT USE THIS UNTIL IT IS COMPLETE ###########
#DO NOT USE
#DO NOT USE

#Create mapping to this for the __init__.py file and main app.py
products = Blueprint('products', __name__, template_folder='templates/products')

@products.route('/newproduct', methods=['GET', 'POST'])
def newproduct():
    form = ProductEntry()
    if form.validate_on_submit():
        product = Product(product_name = form.product_name.data,
								product_description = form.product_description.data, 
								product_price = form.product_price.data, 
								product_quantity = form.product_quantity.data)
        db.session.add(product)
        db.session.commit()
 

        return redirect(url_for('core.index'))

    return render_template('add_product.html', form=form)