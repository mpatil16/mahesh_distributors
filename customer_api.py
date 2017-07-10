from flask import Flask, render_template, request
import customerDao

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def order():
    customer_name = request.form['customer_name']
    date = request.form['date']
    customer_details = customerDao.get_customer(customer_name)
    print("details", customer_name, date)
    print(customer_details)
    return render_template('order_page.html')


# @app.route('/customer/<customer_id>', methods=['GET'])
@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer_info(customer_name):
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
    app.run(host='0.0.0.0')