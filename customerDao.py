import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")


def get_customer(customer_name):
    try:
        cursor = conn.execute("SELECT customer_id, customer_name, address, contact_number, gst_number from customers")
        customer = []
        for row in cursor:
            if row[1] == customer_name:
                customer.append(row[0])
                customer.append(row[1])
                customer.append(row[2])
                customer.append(row[3])
                customer.append(row[4])

    except Exception as e:
        return 'An Error Occurred'

    return customer


def add_customer(customer_id, name, address, contact, gst):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO customers VALUES(?, ?, ?, ?, ?)", (customer_id, name, address, contact, gst))
        conn.commit()

    except Exception as e:
        return 'An Error Occurred'

    return 'Customer Added Successfully'


def get_all():
    customer_list = []
    cursor = conn.execute('select * from customers')
    for row in cursor:
        customer_list.append(row)
    return customer_list


def save_order(products):
    customer_name = products['customer_name']
    date = products['date']
    gst_number = products['gst_number']
    shri_50 = products['shri_50']
    shri_100 = products['shri_100']
    shri_250 = products['shri_250']
    shri_500 = products['shri_500']
    amra_50 = products['amra_50']
    amra_100 = products['amra_100']
    amra_250 = products['amra_250']
    amra_500 = products['amra_500']
    lassi = products['lassi']
    curd_50 = products['curd_50']
    curd_100 = products['curd_100']
    curd_200 = products['curd_200']
    curd_400 = products['curd_400']
    ghee_200 = products['ghee_200']
    ghee_500 = products['ghee_500']
    ghee_1000 = products['ghee_1000']
    cow_200 = products['cow_200']
    cow_500 = products['cow_500']
    cow_1000 = products['cow_1000']
    butter_100 = products['butter_100']
    butter_500 = products['butter_500']
    paneer_200 = products['paneer_200']
    paneer_500 = products['paneer_500']
    plain_tak = products['plain_tak']
    tetra_tak = products['tetra_tak']
    aqua_water = products['aqua_water']
    tetra_lassi = products['tetra_lassi']
    cur = conn.cursor()
    cur.execute("INSERT INTO Records VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"
                " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (customer_name, date, gst_number, shri_50, shri_100, shri_250, shri_500,
                 amra_50, amra_100, amra_250, amra_500, lassi, curd_50,
                 curd_100, curd_200, curd_400, ghee_200, ghee_500, ghee_1000,
                 cow_200, cow_500, cow_1000, butter_100, butter_500, paneer_200
                 , paneer_500, plain_tak, tetra_tak, aqua_water, tetra_lassi))
    conn.commit()


def get_order(customer_name):
    cursor = conn.execute("SELECT * from Records")
    order = []
    for row in cursor:
        if row[0] == customer_name:
            order.append(row[0])
            order.append(row[1])
            order.append(row[2])
            order.append(row[3])
            order.append(row[4])
            order.append(row[5])
            order.append(row[6])
            order.append(row[7])
            order.append(row[8])
            order.append(row[9])
            order.append(row[10])
            order.append(row[11])
            order.append(row[12])
            order.append(row[13])
            order.append(row[14])
            order.append(row[15])
            order.append(row[16])
            order.append(row[17])
            order.append(row[18])
            order.append(row[19])
            order.append(row[20])
            order.append(row[21])
            order.append(row[22])
            order.append(row[23])
            order.append(row[24])
            order.append(row[25])
            order.append(row[26])
            order.append(row[27])
            order.append(row[28])
            order.append(row[29])
    print(order)
