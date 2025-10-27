# config.py

class Config:
    DEBUG = True
    SECRET_KEY = '19AcademiA76'
    
    # Configuración de la base de datos MariaDB
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USER = 'charlyporty'
    DB_PASSWORD = '19NataliA76'
    DB_NAME = 'asistencia_db'

    # URI para SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

