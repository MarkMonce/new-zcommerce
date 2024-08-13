
#Product views.py
from flask import render_template,url_for,redirect,request,Blueprint
from zcommerce import db
from zcommerce.models import Product
from zcommerce.products.forms import ProductEntry


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
 
        return redirect(url_for('products.productlist'))

    return render_template('add_product.html', form=form)

@products.route('/productlist')
def productlist():
    products = Product.query.all()
    return render_template('product_list.html', products=products)

@products.route('/updateproduct/<int:product_id>', methods=['GET', 'POST'])
def updateproduct(product_id):
    product = Product.query.get(product_id)
    form = ProductEntry()
    if form.validate_on_submit():
        
        product.product_name = form.product_name.data
        product.product_description = form.product_description.data
        product.product_price = form.product_price.data
        product.product_quantity = form.product_quantity.data
        
        
        db.session.commit() 
        return redirect(url_for('products.productlist'))
    
    elif request.method == 'GET':
        form.product_name.data = product.product_name
        form.product_description.data = product.product_description
        form.product_price.data = product.product_price
        form.product_quantity.data = product.product_quantity

    return render_template('add_product_old.html', form=form)

@products.route('/deleteproduct/<int:product_id'), methods=['GET', 'POST'])
def deleteproduct(product_id):
    product=Product.query.get(product_id)
    