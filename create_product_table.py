import sqlite3


conn = sqlite3.connect('test.db')

conn.execute('''CREATE TABLE Records(customer_name varchar(50), date date, 
            gst_number varchar(20), shrikhand_50 number(5), shrikhand_100
            number(5), shrikhand_250 number(5), shrikhand_500 number(5),
            amrakhand_50 number(5), amrakhand_100 number(5), amrakhand_250
            number(5), amrakhand_500 number(5), lassi_200 number(5), curd_50 
            number(5), curd_100 number(5), curd_200 number(5), curd_400 
            number(5), buffalo_200 number(5), buffalo_500 number(5), 
            buffalo_1000 number(5), cow_200 number(5), cow_500 number(5), 
            cow_1000 number(5), butter_100 number(5), butter_500 number(5), 
            paneer_200 number(5), paneer_500 number(5), plain_tak number(5),
            aqua_water number(5), tetra_tak number(5), tetra_lassi number(5));''')
print("Table created successfully")

conn.close()
