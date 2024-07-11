#views.py
#Product views.py
from flask import render_template,url_for,redirect,request,Blueprint
###ADD DB STUFF LATER
#from zcommerce import db
#from zcommmerce.models import Customer
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

    return render_template('add_product.html', form=form)