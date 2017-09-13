# A class to make ATL United players
class Player(object): # ALWAYS capitalize class names.
	# Every class needs to start with def __init__
	# This function gets run ONCE and ONLY ONCE, when the object is made.
	# You pass in args when you make the object.
	# self is ALWAYS the first. (It's like "this" in JS.)
	# Everything else is optional.
	def __init__(self, name, daffyDuck, age):
		self.name = name
		self.position = daffyDuck
		self.team = "Atlanta United"
		self.birthyear = 2017 - age
		self.goals_scored = 0
	def trade(self, new_team):
		self.team = new_team
	def change_pos(self, new_position):
		self.old_position = self.position # To conserve the old position.
		self.position = new_position
	def score(self):
		self.goals_scored += 1

player1 = Player('Miguel Almiron', 'midfield', 25)
print player1.name
print player1.position
print player1.team

player2 = Player("Brad Guzan", "goalie", 29)
print player2.name
print player2.position
print player2.team
print player2.birthyear

# player1.team = "Orlando" # Don't do it this way.
# Call a method and let the object manage itself. (Encapsulation)
# Python and JS can't enforce this.
player1.trade("Orlando")
print player1.team
print player1.goals_scored
player1.score()
player1.score()
player1.score()
player1.score()
print player1.goals_scored