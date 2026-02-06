from ..extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(20))  # admin, coach, player, user
    instagram = db.Column(db.String(255))

class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    sport_id = db.Column(db.Integer, db.ForeignKey("sport.id"))
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    is_verified = db.Column(db.Boolean, default=False)