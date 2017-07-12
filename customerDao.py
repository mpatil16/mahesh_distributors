import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")


def get_customer(customer_name):
    cursor = conn.execute("SELECT customer_id, customer_name, address, contact_number, gst_number from customers")
    customer = []
    for row in cursor:
        if row[1] == customer_name:
            customer.append(row[0])
            customer.append(row[1])
            customer.append(row[2])
            customer.append(row[3])
            customer.append(row[4])
    print("customer", customer)
    return customer


def add_customer(customer_id, name, address, contact, gst):
    cur = conn.cursor()
    cur.execute("INSERT INTO customers VALUES(?, ?, ?, ?, ?)", (customer_id, name, address, contact, gst))
    conn.commit()


def get_all():
    customer_list = []
    cursor = conn.execute('select * from customers')
    for row in cursor:
        customer_list.append(row)
    return customer_list
