from app import db


#db model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat = db.Column(db.String(3))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.Integer)
    exp_year = db.Column(db.Integer)
    cvv = db.Column(db.Integer)
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
