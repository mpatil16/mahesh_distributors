import sqlite3


conn = sqlite3.connect('test.db')

conn.execute('''CREATE TABLE products(shrikhand_50 number(5), shrikhand_100
            number(5), shrikhand_250 number(5), shrikhand_500 number(5),
            amrakhand_50 number(5), amrakhand_100 number(5), amrakhand_250
            number(5), amrakhand_500 number(5), lassi_200 number(5), );''')
print("Table created successfully")

conn.close()
