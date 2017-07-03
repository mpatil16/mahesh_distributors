import json

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://SYSTEM:mahesh@localhost:1521/xe'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)


def get_customer():
    customer_info = {}
    customer_info['id'] = 1
    customer_info['name'] = 'Jai Ambe'
    customer_info['address'] = 'Vashi'
    customer_info['contact'] = 9322996920
    customer_info['gst'] = 'mah1234'
    json_customer_info = json.dumps(customer_info)

    return json_customer_info


def add_customer(customer_id, name, address, contact, gst):
    customer_details = {}
    customer_details['id'] = customer_id
    customer_details['name'] = name
    customer_details['address'] = address
    customer_details['contact'] = contact
    customer_details['gst'] = gst

