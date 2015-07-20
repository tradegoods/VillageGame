class Profession(object):

    def __init__(self, game):
        
        self.professionDictionary = {"Farmer": Farmer, "Lumberjack": Lumberjack, "Builder": Builder, "Scout": Scout, "Ranger": Ranger, "Swordsmen": Swordsmen}
    
        
    def add_units(self, game, number):
        if number > game.freePopulation:
            print "You don't have that many dudes"
            return False
        else: 
            self.count += number
            game.freePopulation -= number
            self.update_property(game, number)
	    return True

class Farmer(Profession):
        
        
    def __init__(self, game):

        self.farmerStrength = 3
        game.professionAssigned["Farmer"] = self
        self.count = 0
	self.name = "Farmer"
    def update_property(self, game, number):

        game.foodPerTurn += self.farmerStrength * number

    
class Lumberjack(Profession):
    

    def __init__(self, game):

        self.lumberjackStrength = 3
        game.professionAssigned["Lumberjack"] = self
        self.count = 0
        self.name = "Lumberjack"
    def update_property(self, game, number):

        game.woodPerTurn += self.lumberjackStrength * number


class Builder(Profession):
        
    def __init__(self, game):

        self.builderStrength = 1
        game.professionAssigned["Builder"] = self
        self.count = 0
	self.name = "Builder"


    def update_property(self, game, number):

        game.productivity += self.builderStrength * number


class Scout(Profession):
    
    def __init__(self, game):

        self.scoutDamage = 1
        self.scoutScouting = 3
	self.scoutHealth = 3
        game.professionAssigned["Scout"] = self
        self.count = 0
	self.name = "Scout"

    def update_property(self, game, number):

        game.scouting += self.scoutScouting * number
	game.armyHealth += self.scoutHealth * number
	game.armyDamage += self.scoutDamage * number


class Ranger(Profession):
    
    def __init__(self, game):
        
        self.rangerDamage = 3
	self.rangerHealth = 5
        self.rangerScouting = 3
        game.professionAssigned["Ranger"] = self
        self.count = 0
	self.name = "Ranger"
 
    def update_property(self, game, number):

        game.scouting += number * self.rangerScouting
	game.armyHealth += self.rangerHealth * number
	game.armyDamage += self.rangerDamage * number


class Swordsmen(Profession):
	
	def __init__(self, game):

		self.count = 0
		game.professionAssigned["Swordsmen"] = self
		self.name = "Swordsmen"
		self.swordsmenDamage = 3
		self.swordsmenHealth = 10
	def update_property(self, game, number):
		
		game.armyHealth += self.swordsmenHealth * number
		
		game.armyDamage += self.swordsmenDamage * number
