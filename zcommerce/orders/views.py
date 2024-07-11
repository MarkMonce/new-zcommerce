#order views.py

from flask import render_template,url_for,redirect,request,Blueprint
###ADD DB STUFF LATER
from zcommerce import db
from zcommerce.models import Order, Product, Customer
from zcommerce.orders.forms import OrderEntry
from flask import flash

### DO NOT USE THIS UNTIL IT IS COMPLETE ###########
#DO NOT USE
#DO NOT USE

#Create mapping to this for the __init__.py file and main app.py
orders = Blueprint('orders', __name__, template_folder='templates/orders')

@orders.route('/neworder', methods=['GET', 'POST'])
def neworder():
    form = OrderEntry()
    if form.validate_on_submit():
        product = Product.query.get(form.product_id.data)
        customer = Customer.query.get(form.customer_id.data)
        
        if not product:
            flash('Invalid product ID.', 'danger')
            return redirect(url_for('orders.neworder'))
        
        if not customer:
            flash('Invalid customer ID.', 'danger')
            return redirect(url_for('orders.neworder'))
        
        order = Order(order_date = form.order_date.data,
					customer_id = form.customer_id.data,
                    product_id = form.product_id.data, 
                    order_quantity = form.order_quantity.data)        
        
        order.total = order.order_quantity * product.product_price
        
        if order.order_quantity > product.product_quantity:
                return "Insufficient quantity in stock"
        elif order.total > customer.bank_balance:
                return "Insufficient funds in bank account"
        else:
              product.product_quantity -= order.order_quantity
              customer.bank_balance -= order.total
              
        db.session.add(order)
        db.session.commit()
        


        return redirect(url_for('core.index'))

    return render_template('add_order.html', form=form)