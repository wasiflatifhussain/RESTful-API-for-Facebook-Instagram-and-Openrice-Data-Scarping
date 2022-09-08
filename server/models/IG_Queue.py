# from server import db    #use __main__ instead as python looks for __main__ not for py file name
from sqlalchemy import null
from server import db

class IG_Queue(db.Model):  # object to store data about the tasks in queue for facebook scraping
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"URL: {self.url} | Status: {self.status}"