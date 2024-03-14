from core import create_app
from core.models import User
from core import db

import os

os.environ['FLASK_DEBUG'] = '1'
os.environ['FLASK_RUN_PORT'] = '8000'

app = create_app()

if __name__ == "__main__":
    app.run(debug=True,port=8000)