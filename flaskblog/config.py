# -*- coding: utf-8 -*-

class Config:    
    SECRET_KEY = 'xxx'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'XXX@gmail.com'
    MAIL_PASSWORD = 'XXX'
    #os.environ.get('key')
