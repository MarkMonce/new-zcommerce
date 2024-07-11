#Customer views.py
from flask import render_template,url_for,redirect,request,Blueprint
###ADD DB STUFF LATER
#from zcommerce import db
#from zcommmerce.models import Customer
from zcommerce.customers.forms import CustomerEntry

### DO NOT USE THIS UNTIL IT IS COMPLETE ###########
#DO NOT USE
#DO NOT USE

#Create mapping to this for the __init__.py file and main app.py
customers = Blueprint('customers', __name__, template_folder='templates/customers')

@customers.route('/newcustomer', methods=['GET', 'POST'])
def newcustomer():
    form = CustomerEntry()
    if form.validate_on_submit():
    	##Later, ORM Customer Object will go here to enter form data into database)

    	#db.session.add(customer)
    	#db.session.commit()
    	# firstname = form.firstname.data
    	# lastname = form.lastname.data
    	# address1 = form.address1.data
    	# address2 = form.address2.data
    	# city = form.city.data
    	# state = form.state.data
    	# zipcode = form.zipcode.data
    	# phone = form.phone.data
    	# email = form.city.data
        # bankbalance = form.bankbalance.data

        return redirect(url_for('/'))

    return render_template('add_customer.html', form=form)