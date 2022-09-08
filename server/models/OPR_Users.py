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