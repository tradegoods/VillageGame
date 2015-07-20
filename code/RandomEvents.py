import random

class RandomEvent(object):

	def __init__(self, game):

		roll = random.randint(1, 30)

		if roll == 1:

			self.Bear(game)

		if roll > 1 and roll < 5:
			
			self.Deer(game)

		if roll > 4 and roll < 7:
	
			self.Boar(game)

	def Bear(self, game):

		print "You run into a bear!"
		print "Fight? Yes or no."
		bearHealth = 50
		bearAttack = 10
		choice = ' '
		while not ("yes" in choice or "no" in choice):
			choice = raw_input("Attack: ")
		if "yes" in choice:
			if game.combat(bearHealth, bearAttack):
				print "You gain 30 food"
				game.resources["Food"] += 30
			else:
				print "The bear decides to be merciful even though you lost"
		else:
			print "You decide not to attack."
	def Deer(self, game):
	
		print "You find a deer!"
		print "You gain 10 food"
		game.resources["Food"] += 10
		
	
	def Boar(self, game):

		print "You find a boar!"
		print "Fight? Yes or no."
		boarHealth = 20
		boarAttack = 5
		choice = ' '
		while not ("yes" in choice or "no" in choice):
			choice = raw_input("Attack: ")
		if "yes" in choice:
			if game.combat(boarHealth, boarAttack):
				print "You gain 20 food"
				game.resources["Food"] += 20
			else:
				print "The boar decides to be merciful even though you lost"
		else:
			print "You decide not to attack"


