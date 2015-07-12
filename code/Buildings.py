from Professions import Profession
from Professions import Ranger
class Building(object):


    def __init__(self):
        self.buildingList = {"House": self.Housing, "Fletchery": self.Fletchery, "Forge": self.Forge, "Lumbermill": self.Lumbermill, "Blacksmith": self.Blacksmith} 

    class Fletchery(object):
        
        def __init__(self):
            self.name = "Fletchery"
            self.cost = 5

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
        pass

    class Housing(object):
        
        def __init__(self):
            self.name = "House"
            self.cost = 3

        def complete(self, game):
            print "You built a house"
