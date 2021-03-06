from app import db

class Player(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(32), index = True, unique = True)
	main = db.Column(db.String(32), index = True)
	ranking = db.Column(db.Integer, index = True, unique = True)
	description = db.Column(db.String(512), index = True)

	def __repr__(self):
		return '<Player %r>' % (self.nickname)

	def __cmp__(self, other):
		return cmp(self.ranking, other.ranking)