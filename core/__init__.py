from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import platform

from .config import ProductionConfig,  DevelopmentConfig


if platform.system() =="Windows":   

    app_config=DevelopmentConfig()
else:
    app_config=ProductionConfig()



db = SQLAlchemy()

def create_app():
    global db
    global app_config
   

    app = Flask(__name__,
                template_folder=app_config.TEMPLATE_FOLDER,
                static_folder=app_config.STATIC_FOLDER)
            
    app.config.from_object(app_config)
    db.init_app(app)

    from .models import User

    create_database(app)
    #import models to init migration
   
    migrate = Migrate(app,db)



    from auth.views import auth
    from agents.views import agents_bp
    from customers.views import customers_bp

    app.register_blueprint(auth)
    app.register_blueprint(agents_bp)
    app.register_blueprint(customers_bp)

    login_manager=LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "authentication_blueprint.login"

    

    @login_manager.user_loader
    def load_user(id):
        try:
            return User.query.get(int(id))
        except:
            return None
        
    return app


def create_database(app=Flask):
    
    with app.app_context():
        if not os.path.exists(app.config['DB_NAME']):
            db.create_all()
            db.session.commit()
            print('Created Database!')
        from .models import User

        existing_user = User.query.filter_by(email='admin@app').first()
        if not existing_user:
            default_user = User(username='admin', email='admin@app', password='admin',agent=True)
            db.session.add(default_user)
            db.session.commit()




