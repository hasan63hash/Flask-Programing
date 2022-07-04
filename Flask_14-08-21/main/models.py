from main import db
from datetime import datetime

class SQLAlchemyJSONEncoder:
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Image(db.Model, SQLAlchemyJSONEncoder):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(150), unique=True, nullable=False)
    file_path = db.Column(db.String(50), nullable=False, default="static/images/")
    entry_date = db.Column(db.String(10), nullable=False, default=datetime.now().strftime("%d/%m/%Y"))

    def __init__(self, file_name):
        self.file_name = file_name

    def __repr__(self):
        return f"{self.file_name}"
