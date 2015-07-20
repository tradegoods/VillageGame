class Location(object):

	def __init__(self):

		self.locationDictionary = {"Mines": Mines, "Enemy Village": EnemyVillage}


class Mines(Location):

	def discovery(self, game):
		
		print "You have discovered a Goblin Infested Mine!"
		self.name = "Mines"
		game.discoveredLocation[self.name] = self
		self.locationHealth = 250
		self.locationAttack = 10
		

	def spoils(self, game):

		print "You can now build a blacksmith"
		game.availableBuildings.append("Blacksmith")



	
class EnemyVillage(Location):


	def discovery(self, game):

		print "You have discovered the Enemy Village!"
		self.name = "Enemy Village"
		game.discoveredLocation[self.name] = self
		self.locationHealth = 1000
		self.locationAttack = 20


	def spoils(self, game):
		
		print "You win!"
