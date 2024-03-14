import os
from pathlib import Path

class Config(object):
    """Base config, uses staging database server."""
    TESTING = False

    
    BASE_DIR=str(Path(__file__).parent.parent)
    TEMPLATE_FOLDER= os.path.join(BASE_DIR,'templates')
    STATIC_FOLDER= os.path.join(BASE_DIR,'static')
    UPLOAD_FOLDER = os.path.join(STATIC_FOLDER,"uploads")
    FILES_FOLDER = os.path.join(STATIC_FOLDER,"files")
    EXPORT_FOLDER = os.path.join(STATIC_FOLDER,"export")
    PAYSLIPS_FOLDER = os.path.join(STATIC_FOLDER,"zip")

    SECURITY_PASSWORD_SALT = 'my_precious_two'

    SQLALCHEMY_TRACK_MODIFICATIONS=True




    

class ProductionConfig(Config):

    BASE_DIR=str(Path(__file__).parent.parent)
    """Uses production database server."""   
    SECRET_KEY = os.getenv("SECRET_KEY", default = "oijhjkolhkjhojhwgwsergsdbterjhedngjtrngdbdfg=")
    DB_NAME= os.path.join(BASE_DIR,'database.db')
    SQLALCHEMY_DATABASE_URI= f'sqlite:///{DB_NAME}'


class DevelopmentConfig(Config):

    BASE_DIR=str(Path(__file__).parent.parent)
    SECRET_KEY = os.getenv("SECRET_KEY", default = "oijhjkolhkjhojh")
    DB_NAME= os.path.join(BASE_DIR,'database.db')
    SQLALCHEMY_DATABASE_URI= f'sqlite:///{DB_NAME}'



