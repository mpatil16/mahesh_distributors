from flask import Flask, render_template, request
from customer_service import *
app = Flask(__name__)


@app.route('/customer', methods = ['GET'])
def get_customer_info():
    customer = get_customer()
    # render_template('customer_page.html')
    return customer


@app.route('/customer/add', methods=['GET','POST'])
def add_new_customer():
    if request.method == 'POST':
        customer_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        gst = request.form['gst']
        add_customer(customer_id, name, address, contact, gst)
        return 'Added Sucessfully'
    return render_template('add_customer.html')


if __name__ == '__main__':
   app.run()