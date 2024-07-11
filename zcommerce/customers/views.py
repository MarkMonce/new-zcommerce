#Customer views.py
from flask import render_template,url_for,redirect,request,Blueprint
###ADD DB STUFF LATER
from zcommerce import db
from zcommerce.models import Customer
from zcommerce.customers.forms import CustomerEntry


#Create mapping to this for the __init__.py file and main app.py
customers = Blueprint('customers', __name__, template_folder='templates/customers')

@customers.route('/newcustomer', methods=['GET', 'POST'])
def newcustomer():
    form = CustomerEntry()
    if form.validate_on_submit():
        customer = Customer(first_name = form.firstname.data,
                                last_name = form.lastname.data, 
                                address1 = form.address1.data, 
                                address2 = form.address2.data,
                                city = form.city.data, 
                                state = form.state.data, 
                                zipcode = form.zipcode.data,
                                phone = form.phone.data,
                                email = form.email.data,
                                bank_balance = form.bankbalance.data)
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('add_customer.html', form=form)