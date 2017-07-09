from flask import Flask, render_template, request
import customerDao
app = Flask(__name__)


@app.route('/customer/', methods=['GET'])
def get_customer_info():
    customer_name = 'Jai Ambe'
    customer = customerDao.get_customer(customer_name)
    return 'Hello'


@app.route('/customer/add', methods=['GET','POST'])
def add_new_customer():
    if request.method == 'POST':
        customer_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        gst = request.form['gst']
        customerDao.add_customer(customer_id, name, address, contact, gst)
        return 'Added Sucessfully'
    return render_template('add_customer.html')


if __name__ == '__main__':
   app.run()