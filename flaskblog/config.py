# -*- coding: utf-8 -*-

class Config:    
    SECRET_KEY = 'a3071285de7d178a7ab64619baa691ed'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'XXX@gmail.com'
    MAIL_PASSWORD = 'XXX'
    #os.environ.get('key')