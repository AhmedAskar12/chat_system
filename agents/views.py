from flask import Blueprint, render_template
from flask_login import current_user

agents_bp = Blueprint('agents', __name__, template_folder='templates/agents')

@agents_bp.route('/agents')
def agent_dashboard():
    return render_template('agents/agent_dashboard.html')
