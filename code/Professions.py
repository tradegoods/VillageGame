class Profession(object):

    def __init__(self):
        
        self.professionDictionary = {"Farmer": Farmer, "Lumberjack": Lumberjack, "Builder": Builder, "Scout": Scout}
    

    def add_units(self, game, number):
        if number > game.freePopulation:
            print "You don't have that many dudes"
        else: 
            self.count += number
            game.freePopulation -= number
            self.update_property(game)

class Farmer(Profession):
        
        
    def __init__(self):

        self.farmerStrength = 3
        
        self.count = 0

    def update_property(self, game):

        game.foodPerTurn = self.farmerStrength * self.count - game.population

    
class Lumberjack(Profession):
     pass


class Builder(Profession):
        
    def __init__(self):

        self.builderStrength = 1

        self.count = 0

    def update_property(self, game):

        game.productivity = self.builderStrength * self.count


class Scout(Profession):
    pass
