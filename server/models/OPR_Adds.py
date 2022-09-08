# from server import db    #use __main__ instead as python looks for __main__ not for py file name
from sqlalchemy import null
from server import db

class OPR_Adds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    
    def __repr__(self):
        return f"URL: {self.url}"