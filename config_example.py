import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:password@mysqlip/DBname?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
