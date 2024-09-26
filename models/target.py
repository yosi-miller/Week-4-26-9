from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Target(db.Model):
    __tablename__ = 'target'

    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('target_country.id'), nullable=False)
    mission_date = db.Column(db.Date, nullable=True)
    city = db.Column(db.String(100), nullable=True)
    target_priority = db.Column(db.String(100), nullable=True)
    target_latitude = db.Column(db.String(100), nullable=True)
    target_longitude = db.Column(db.String(100), nullable=True)
