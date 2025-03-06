from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy(app)

# Database Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(255))

# Home Route
@app.route('/')
def home():
    categories = ['Televisions', 'Audio', 'Home Appliances', 'Kitchen Appliances']
    products = Product.query.all()
    return render_template('index.html', products=products, categories=categories)

# Product Filtering
@app.route('/category/<string:category>')
def filter_category(category):
    products = Product.query.filter_by(category=category).all()
    return render_template('index.html', products=products, categories=[category])

# Lead Generation Form
@app.route('/inquiry', methods=['POST'])
def inquiry():
    name = request.form['name']
    mobile = request.form['mobile']
    category = request.form['category']
    message = request.form['message']
    new_lead = Lead(name=name, mobile=mobile, category=category, message=message)
    db.session.add(new_lead)
    db.session.commit()
    return redirect(url_for('home'))

# Admin Panel (Adding Products)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        description = request.form['description']
        new_product = Product(name=name, category=category, price=price, description=description)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('admin'))
    
    products = Product.query.all()
    return render_template('admin.html', products=products)

@app.route('/admin/inquiries')
def admin_inquiries():
    inquiries = Lead.query.all()
    return render_template('inquiries.html', inquiries=inquiries)


# Run App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



