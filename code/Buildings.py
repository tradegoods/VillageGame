from Professions import Profession
from Professions import Ranger
from Professions import Swordsmen
class Building(object):


    def __init__(self):
        self.buildingList = {"House": self.Housing, "Fletchery": self.Fletchery, "Forge": self.Forge, "Lumbermill": self.Lumbermill, "Blacksmith": self.Blacksmith} 

    class Fletchery(object):
        
        def __init__(self):
            self.name = "Fletchery"
            self.woodCost = 5
            self.productionCost = 10

        def complete(self, game):
            game.availableBuildings.remove("Fletchery")
            game.availableProfessions.append("Ranger")
            Ranger(game)
            print "You finished the fletchery"
    
    class Forge(object):
        pass

    class Lumbermill(object):
        pass

    class Blacksmith(object):
        
	def __init__(self):
	
		self.name = "Blacksmith"
		self.woodCost = 50
		self.productionCost = 20

	def complete(self, game):
		game.availableBuildings.remove("Blacksmith")
		game.availableProfessions.append("Swordsmen")
		Swordsmen(game)
		print "You built a blacksmith"

    class Housing(object):
        
        def __init__(self):
            self.name = "House"
            self.woodCost = 3
            self.productionCost = 5

        def complete(self, game):
            print "You built a house"
