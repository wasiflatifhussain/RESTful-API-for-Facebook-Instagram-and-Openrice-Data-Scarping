# from server import db    #use __main__ instead as python looks for __main__ not for py file name
from sqlalchemy import null
from server import db


class OPR_Users(db.Model):  # object to store the info about each individual user for openrice
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    level = db.Column(db.String(50), nullable=False)
    followings = db.Column(db.String(50), nullable=False)
    followers = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"UserID: {self.name} | User Level: {self.level} | User's Following: {self.followings} | User's Followers: {self.followers}"


class OPR_Queue(db.Model):  # object to store data about the tasks in queue
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"URL: {self.url} | Status: {self.status}"


class FB_Users(db.Model):  # facbook user object to store each user info
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    friends = db.Column(db.String(100), nullable=False)
    #followers = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"UserID: {self.userid} | Name: {self.name} | Friend Number: {self.friends}"


class FB_Queue(db.Model):  # object to store data about the tasks in queue for facebook scraping
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"URL: {self.url} | Status: {self.status}"
    

class OPR_Adds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    
    def __repr__(self):
        return f"URL: {self.url}"
 
    
class FB_Adds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    
    def __repr__(self):
        return f"URL: {self.url}"
