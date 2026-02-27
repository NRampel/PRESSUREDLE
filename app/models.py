from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False) 

    games_played = db.Column(db.Integer, default=0) 
    games_won = db.Column(db.Integer, default=0) 
    current_streak = db.Column(db.Integer, default=0)
    games_lost = db.Column(db.Integer, default=0)
    monsters_discovered = db.relationship('discoveredMonsters', backref='finder', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class discoveredMonsters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monster_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
