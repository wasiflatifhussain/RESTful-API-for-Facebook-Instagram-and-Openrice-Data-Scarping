# from server import db    #use __main__ instead as python looks for __main__ not for py file name
from sqlalchemy import null
from server import db

class IG_Users(db.Model):  # facbook user object to store each user info
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    followers = db.Column(db.String(100), nullable=False)
    followings = db.Column(db.String(100), nullable=False)
    #followers = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"UserID: {self.username} | Name: {self.followers} | Friend Number: {self.followings}"