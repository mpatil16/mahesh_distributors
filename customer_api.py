from flask import Flask, render_template, request
import customerDao

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def order():
    print("inside order route")
    customer_name = request.form['customer_list']
    date = request.form['date']
    print("Still inside")
    customer_details = customerDao.get_customer(customer_name)
    gst_number = customer_details[4]
    print(customer_name, gst_number, date)
    return render_template('order_page.html', customer_names=customer_name, dates=date, gst_numbers=gst_number)


@app.route('/customer_name/<customer_name>', methods=['GET'])
def get_customer_info(customer_name):
    customer = customerDao.get_customer(customer_name)
    return render_template('customer_details.html', customers=customer)


@app.route('/customer/add', methods=['GET', 'POST'])
def add_new_customer():
    if request.method == 'POST':
        customer_id = request.form['id']
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        gst = request.form['gst']
        customerDao.add_customer(customer_id, name, address, contact, gst)
        return render_template('add_customer.html')
    return render_template('add_customer.html')


@app.route('/customers')
def get_all_customers():
    customer_list = customerDao.get_all()
    return render_template('customer_details_page.html', customer_lists=customer_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0')