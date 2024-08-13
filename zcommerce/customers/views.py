#Customer views.py
from flask import render_template,url_for,redirect,request,Blueprint
from zcommerce import db
from zcommerce.models import Customer
from zcommerce.customers.forms import CustomerEntry


#Create mapping to this for the __init__.py file and main app.py
customers = Blueprint('customers', __name__, template_folder='templates/customers')

@customers.route('/newcustomer', methods=['GET', 'POST'])
def newcustomer():
    form = CustomerEntry()
    if form.validate_on_submit():
        customer = Customer(first_name=form.firstname.data,
                            last_name=form.lastname.data,
                            address1=form.address1.data,
                            address2=form.address2.data,
                            city=form.city.data,
                            state=form.state.data,
                            zipcode=form.zipcode.data,
                            phone=form.phone.data,
                            email=form.email.data,
                            bank_balance=form.bankbalance.data)

        db.session.add(customer)
        db.session.commit()

        return redirect(url_for('customers.customerlist'))

    return render_template('add_customer.html', form=form)

#route to display all customers using a query and customer_list.html

@customers.route('/customerlist')
def customerlist():
    customers = Customer.query.all()
    return render_template('customer_list.html', customers=customers)

#create a route to update a customer
#customer_id is passed in as an argument from the href in the customer_list.html file


@customers.route('/updatecustomer/<int:customer_id>', methods=['GET', 'POST'])
def updatecustomer(customer_id):
    customer = Customer.query.get(customer_id)
    form = CustomerEntry()

    if form.validate_on_submit():
        customer.first_name = form.firstname.data
        customer.last_name = form.lastname.data
        customer.address1 = form.address1.data
        customer.address2 = form.address2.data
        customer.city = form.city.data
        customer.state = form.state.data
        customer.zipcode = form.zipcode.data
        customer.phone = form.phone.data
        customer.email = form.email.data
        customer.bank_balance = form.bankbalance.data

        db.session.commit()
        return redirect(url_for('customers.customerlist'))

    elif request.method == 'GET':
        form.firstname.data = customer.first_name
        form.lastname.data = customer.last_name
        form.address1.data = customer.address1
        form.address2.data = customer.address2
        form.city.data = customer.city
        form.state.data = customer.state
        form.zipcode.data = customer.zipcode
        form.phone.data = customer.phone
        form.email.data = customer.email
        form.bankbalance.data = customer.bank_balance

    return render_template('add_customer.html', form=form)


