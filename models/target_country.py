from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TargetCountry(db.Model):
    __tablename__ = 'target_country'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name
