import os

class Config:
    SECRET_KEY = 'your_secret_key'
    #SQLALCHEMY_DATABASE_URI 
    # # Update this line to match your folder structure
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.path.dirname(__file__), "../database/rules.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


