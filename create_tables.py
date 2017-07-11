import sqlite3


conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE customers( customer_id number(10) NOT NULL,  
            customer_name varchar2(50) NOT NULL,  address varchar2(50) NOT NULL,
            contact_number number(10) NOT NULL,  gst_number varchar2(20) NOT NULL, 
                CONSTRAINT customer_pk PRIMARY KEY (customer_id));''')
print("Table created successfully")

conn.close()
