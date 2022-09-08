class Config(object):
  DEBUG  =False
  TESTING = False
  
  # SECRET_KEY = "abcdefghijkl"
  
  DB_NAME = "production-db"
  DB_USERNAME = "root"
  DB_PASSWORD = "example"

  FB_EMAIL = "litroint@gmail.com"
  FB_PASS = "litroTEAM5435"
  
  # FB_TIME = 1200
  # OPR_TIME = 900
  
  FB_TIME = 30
  OPR_TIME = 30
  IG_TIME = 30
  
  INTERVAL = 10
  
  #UPLOAD = "/home/username/app/app/static/images/uploads"
  
  SESSION_COOKIE_SECURE = True
  
class ProductionConfig(Config):  #will take in all attributes from class Config
  FB_TIME = 1200
  OPR_TIME = 900
  IG_TIME = 900

class DevelopmentConfig(Config):
  DEBUG= True
  
  DB_NAME = "development-db"
  DB_USERNAME = "root"
  DB_PASSWORD = "example"

  #UPLOAD = "/home/username/project/app/app/static/images/uploads"
  
  SESSION_COOKIE_SECURE = False
  
class TestingConfig(Config):
  TESTING = True
  
  DB_NAME = "development-db"
  DB_USERNAME = "root"
  DB_PASSWORD = "example"

  #UPLOAD = "/home/username/project/app/app/static/images/uploads"

  SESSION_COOKIE_SECURE = False