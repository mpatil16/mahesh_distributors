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
    print('Inside order route')
    customer_name = request.form['customer_list']
    print('Customer Name', customer_name)
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
        print(products['customer_name'])
        products['date'] = request.form['date']
        products['gst_number'] = request.form['gst_number']
        print(products['gst_number'])
        products['shri_50'] = request.form['shrikhand_50']
        products['shri_100'] = request.form['shrikhand_100']
        products['shri_250'] = request.form['shrikhand_250']
        products['shri_500'] = request.form['shrikhand_500']
        products['shri_loose'] = request.form['shrikhand_loose']
        products['amra_50'] = request.form['amrakhand_50']
        products['amra_100'] = request.form['amrakhand_100']
        products['amra_250'] = request.form['amrakhand_250']
        products['amra_500'] = request.form['amrakhand_500']
        products['amra_loose'] = request.form['amrakhand_loose']
        products['keshar_250'] = request.form['keshar_250']
        products['keshar_500'] = request.form['keshar_500']
        products['lassi'] = request.form['lassi']
        products['tetra_lassi'] = request.form['tetra_lassi']
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
        products['masala_tak'] = request.form['masala_tak']
        products['tetra_tak'] = request.form['tetra_tak']
        products['aqua_water'] = request.form['aqua_water']
        products['flavoured'] = request.form['flavoured']
        products['juice'] = request.form['juice']
        products['cheese'] = request.form['cheese']
        products['smp'] = request.form['smp']
        customerDao.save_order(products)
    return 'Order Saved'


@app.route('/get_order/<customer_name>')
def get_order_details(customer_name):
    customerDao.get_order(customer_name)
    return 'Get Order Details'


@app.route('/bill_details', methods=['GET'])
def bill_details():
    return render_template('bill_details_page.html')


@app.route('/print_bill', methods=['POST'])
def print_bill():
    customer_name = request.form['customer_list']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    customerDao.get_order_detail(customer_name, start_date, end_date)
    return 'Printing bill'


@app.route('/customer_name/<customer_name>', methods=['GET'])
def get_customer_info(customer_name):
    customer = customerDao.get_customer(customer_name)
    return render_template('customer_details_page.html', customers=customer)


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
