import random

class RandomEvent(object):

	def __init__(self, game):

		roll = random.randint(1, 30)

		if roll == 1:

			self.Bear()

		if roll > 1 and roll < 5:
			
			self.Deer(game)

		if roll > 4 and roll < 7:
	
			self.Boar()

	def Bear(self):

		print "You run into a bear!"

	def Deer(self, game):
	
		print "You find a deer!"
		game.resources["Food"] += 20
		
	
	def Boar(self):

		print "You find a boar!"
