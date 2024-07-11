# models.py

from zcommerce import db

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    address1 = db.Column(db.String(128))
    address2 = db.Column(db.String(128))
    city = db.Column(db.String(64))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(10))
    email = db.Column(db.String(128), unique=True)
    phone = db.Column(db.String(20))
    bank_balance = db.Column(db.Float)
    orders = db.relationship('Order', backref='customer', lazy='dynamic')

    def __init__(self, first_name, last_name, address1, address2, city, state, zipcode, email, phone, bank_balance=1000.0):
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.email = email
        self.phone = phone
        self.bank_balance = bank_balance

    def __repr__(self):
        return f"Customer: {self.first_name} {self.last_name}"
    
    # def bank_balance(self):
    #     return self.bankbalance
    
    def update_bank_balance(self, amount):
        self.bankbalance += amount
        return self.bankbalance


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64))
    product_description = db.Column(db.String(128))
    product_price = db.Column(db.Float)
    product_quantity = db.Column(db.Integer)
    orders = db.relationship('Order', backref='product', lazy='dynamic')

    def __init__(self, product_name, product_description, product_price, product_quantity):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_quantity = product_quantity

    def __repr__(self):
        return f"Product: {self.product_name}"
    
    # def product_price(self):
    #     return self.product_price
    
    # def product_quantity(self):
    #     return self.product_quantity
    
    def update_product_quantity(self, amount):
        self.product_quantity += amount
        return self.product_quantity
    
    def update_product_price(self, amount):
        self.product_price += amount
        return self.product_price
    
    def update_product_description(self, description):
        self.product_description = description
        return self.product_description
    
    def update_product_name(self, name):
        self.product_name = name
        return self.product_name


class Order(db.Model):
    
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.Integer, db.ForeignKey('customers.id'))
    productid  = db.Column(db.Integer, db.ForeignKey('products.id'))
    order_date = db.Column(db.Date, nullable=False)
    order_quantity = db.Column(db.Integer)
    total = db.Column(db.Float)
    
    def __init__(self, customer_id, product_id, order_date, order_quantity, total=0.0):
        self.customerid = customer_id
        self.productid = product_id
        self.order_date = order_date
        self.order_quantity = order_quantity
        self.total = total
    
    def __repr__(self):
        return f"Order: {self.id}"
    

    
    def update_total(self, quantity, price):
        self.total = quantity * price
        return self.total
    
    def sufficient_stock(self, product_quantity):
        if self.quantity <= product_quantity:
            return True
        else:
            return False
        
    def sufficient_bank_balance(self, bank_balance):
        if self.total <= bank_balance:
            return True
        else:
            return False



