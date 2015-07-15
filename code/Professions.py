class Profession(object):

    def __init__(self, game):
        
        self.professionDictionary = {"Farmer": Farmer, "Lumberjack": Lumberjack, "Builder": Builder, "Scout": Scout, "Ranger": Ranger}
    
        
    def add_units(self, game, number):
        if number > game.freePopulation:
            print "You don't have that many dudes"
        else: 
            self.count += number
            game.freePopulation -= number
            self.update_property(game)

class Farmer(Profession):
        
        
    def __init__(self, game):

        self.farmerStrength = 3
        game.professionAssigned["Farmer"] = self
        self.count = 0
	self.name = "Farmer"
    def update_property(self, game):

        game.foodPerTurn = self.farmerStrength * self.count - game.population

    
class Lumberjack(Profession):
     pass


class Builder(Profession):
        
    def __init__(self, game):

        self.builderStrength = 1
        game.professionAssigned["Builder"] = self
        self.count = 0
	self.name = "Builder"


    def update_property(self, game):

        game.productivity = self.builderStrength * self.count


class Scout(Profession):
    
    def __init__(self, game):

        self.scoutDamage = 1
        self.scoutScouting = 3
        game.professionAssigned["Scout"] = self
        self.count = 0
	self.name = "Scout"

    def update_property(self, game):

        game.scouting = self.count * self.scoutScouting



class Ranger(Profession):
    
    def __init__(self, game):
        
        self.rangerDamage = 3
        self.rangerScouting = 3
        game.professionAssigned["Ranger"] = self
        self.count = 0
	self.name = "Ranger"
 
    def update_property(self, game):

        game.scouting = self.count * self.rangerScouting + game.professionAssigned["Scout"].count * game.professionAssigned["Scout"].scoutScouting
