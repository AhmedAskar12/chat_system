from flask import Blueprint, render_template

customers_bp = Blueprint('customers', __name__, template_folder='templates/customers')

@customers_bp.route('/')
def customer_dashboard():
    return render_template('customers/customer_dashboard.html')
