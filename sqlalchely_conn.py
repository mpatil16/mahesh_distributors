from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///test.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


class customer(db.Model):
    customer_id = db.Column(db.Integer(10), primary_key=True)
    # customer_name = db.Column(db.String(100))
    # address = db.Column(db.String(100))
    # contact_number = db.Column(db.String(12), unique=True)
    # gst_number = db.Column(db.String(12), unique=True)

    def __init__(self, customer_id):
        self.id = id
    # def __init__(self, id, customer_name, address, contact_number, gst_number):
    #     self.id = id
    #     self.customer_name = customer_name
    #     self.address = address
    #     self.contact_number = contact_number
    #     self.gst_number = gst_number


@app.route('/')
def first():
    customers = customer(1)
    return render_template('show_all.html', customer=customers.query.all())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
