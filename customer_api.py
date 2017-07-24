from flask import Flask, render_template, request
import customerDao
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def order():
    customer_name = request.form['customer_list']
    date = request.form['date']
    customer_details = customerDao.get_customer(customer_name)
    gst_number = customer_details[4]
    return render_template('order_page.html', customer_names=customer_name, dates=date, gst_numbers=gst_number)


@app.route('/save_order', methods=['POST'])
def save_products():
    if request.method == 'POST':
        print("inside save_order route")
        products = {}
        customer_name = request.form['customer_name']
        print(customer_name)
        products['customer_name'] = request.form['customer_name']
        products['date'] = request.form['date']
        products['gst_number'] = request.form['gst_number']
        products['shri_50'] = request.form['shrikhand_50']
        products['shri_100'] = request.form['shrikhand_100']
        products['shri_250'] = request.form['shrikhand_250']
        products['shri_500'] = request.form['shrikhand_500']
        products['amra_50'] = request.form['amrakhand_50']
        products['amra_100'] = request.form['amrakhand_100']
        products['amra_250'] = request.form['amrakhand_250']
        products['amra_500'] = request.form['amrakhand_500']
        products['lassi'] = request.form['lassi']
        products['curd_50'] = request.form['curd_50']
        products['curd_100'] = request.form['curd_100']
        products['curd_200'] = request.form['curd_200']
        products['curd_400'] = request.form['curd_400']
        products['ghee_200'] = request.form['ghee_200']
        products['ghee_500'] = request.form['ghee_500']
        products['ghee_1000'] = request.form['ghee_1000']
        products['cow_200'] = request.form['cow_ghee_200']
        products['cow_500'] = request.form['cow_ghee_500']
        products['cow_1000'] = request.form['cow_ghee_1000']
        products['butter_100'] = request.form['butter_100']
        products['butter_500'] = request.form['butter_500']
        products['paneer_200'] = request.form['paneer_200']
        products['paneer_500'] = request.form['paneer_500']
        products['plain_tak'] = request.form['plain_tak']
        products['tetra_tak'] = request.form['tetra_tak']
        products['aqua_water'] = request.form['aqua_water']
        products['tetra_lassi'] = request.form['tetra_lassi']
        customerDao.save_order(products)
    return 'Order Saved'


@app.route('/get_order/<customer_name>')
def get_order_details(customer_name):
    customerDao.get_order(customer_name)
    return 'Get Order Details'


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