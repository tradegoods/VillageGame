from Buildings import Building
from Professions import Profession
from RandomEvents import RandomEvent
from Locations import Location
class Engine(object):
        
    
    
    def __init__(self):
        self.productivity = 0
        self.population = 80
        self.freePopulation = 80
        self.completeProjects = []
        self.availableBuildings = ["House", "Fletchery"]
        self.currentProjects = []
        self.availableProfessions = ["Builder", "Farmer", "Scout", "Lumberjack"]
        self.professionAssigned = {}
        self.commandDictionary = {"help": self.helpout, "Stockpile": self.stockpile, "Population": self.population_status, "Build": self.available_buildings, "Assign Dudes": self.assign_dudes,                                  "Attack": self.attack_location}
        self.resources = {"Wood": 5, "Food": 10}
        self.foodPerTurn = -8
        self.woodPerTurn = 0
        self.scoutingRequirement = {"Mines": 100, "Enemy Village": 300}
        self.mapExplored = 0
        self.discoveredLocation = {}
        self.armyHealth = 0
        self.armyDamage = 0
        self.scouting = 0
    def month_sequence(self):
        if len(self.currentProjects) == 0:
            print "You have no current projects"
        else:
            for project in self.currentProjects:
                project.cost -= self.productivity    
                if project.cost <= 0:
                    self.completeProjects.append(project)
                else:
                    print "%s will be done in %r turns" % (project.name, (project.cost / self.productivity + (project.cost % self.productivity != 0)))
        print "The following projects are completed:"
        if len(self.completeProjects) == 0:
            print "None"
        for project in self.completeProjects:
            print project.name
            project.complete(self)
            self.currentProjects.remove(project)
        self.completeProjects = []
        print "~~~~~~~~~~"
        print "Would you like to start something else?"
        print "Available Buildings:"
        for building in self.availableBuildings:
            print building
        choice = " "
        while choice != "no":
            choice = raw_input("> ")
            if choice in self.availableBuildings:
                if choice in self.currentProjects:
                    print "Already Doing that Scrub"
                else:
                    project = Building().buildingList[choice]()
                    self.currentProjects.append(project)
                    print "%s will be done in %r turns" % (project.name, (project.cost / self.productivity + (project.cost % self.productivity != 0)))
        self.run_month()

    def run_month(self):
        
        print("Reassign Dudes?")
        choice = " "
        while not "no" in choice:
            choice = raw_input("> ").split(" ")
            if choice[0] in self.availableProfessions:
                number = int(choice[1])
                self.professionAssigned[choice[0]].add_units(self, number)    

        self.month_sequence()
    

    def turn_sequence(self):

        self.upkeep()
        self.explore()
        while True:
                
            choice = raw_input("> ")            
        
            if choice == '':
            
                break       

            if choice in self.commandDictionary:
                    
                self.commandDictionary[choice]()
                
            else:
                    
                print "I don't understand that command"
            
        self.turn_sequence()

    def upkeep(self):

        self.resources["Food"] += self.foodPerTurn
        self.resources["Wood"] += self.woodPerTurn
        for project in self.currentProjects:
            project.productionCost -= self.productivity    
            if project.productionCost <= 0:
                self.completeProjects.append(project)
            for project in self.completeProjects:
                project.complete(self)
                self.currentProjects.remove(project)
        self.completeProjects = []

    def explore(self):
   
        RandomEvent(game)
        self.mapExplored += self.scouting
        removeList = []
        for location in self.scoutingRequirement:
            if self.mapExplored >= self.scoutingRequirement[location]:
                Location().locationDictionary[location]().discovery(self)
                removeList.append(location)
        for element in removeList:
            del self.scoutingRequirement[element]       
 
    def stockpile(self):
        
        for resource in self.resources:
        
            print "You have %d  %s" % (self.resources[resource], resource)

    def population_status(self):

        print "Total population %d" % (self.population)
        print "Avaiable Population %d" %(self.freePopulation)
        for profession in self.professionAssigned:
        
            print "You have %d %ss" % (self.professionAssigned[profession].count, profession)

    def available_buildings(self):
    

        print "Available Buildings:"
        for building in self.availableBuildings:
            print building
        choice = " "
        while choice != "done":
            choice = raw_input("> ")
            if choice in self.availableBuildings:
                if choice in self.currentProjects:
                    print "Already Doing that Scrub"
                
                elif self.productivity == 0:
            
                    print "You got no builders dawg"


                else:
                    project = Building().buildingList[choice]()
                    if project.woodCost < self.resources["Wood"]:
                        self.currentProjects.append(project)
                        self.resources["Wood"] -= project.woodCost
                        print "%s will be done in %r turns" % (project.name, (project.productionCost / self.productivity + (project.productionCost % self.productivity != 0)))
                    else:
                        print "Not enough Wood"

    def assign_dudes(self):

        print("Reassign Dudes?")
        finished = False
        while not finished:
            choice = raw_input("> ").split(" ") 
            if "done" in choice:
                break
            
            if choice[0] in self.availableProfessions:
                number = choice[1]
                if False in [number[i] in '-0123456789' for i in range(0, len(number))]:
                    print "That's not a number"
                else:
                    number = int(number)
                    self.professionAssigned[choice[0]].add_units(self, number)                  
    
            else: 
                print "I don't know what that is"    
    
    def attack_location(self):

        print("Which location would you like to attack?")
        for location in self.discoveredLocation:
            print location
        finished = False
        while not finished:
            choice = raw_input("Attack: ")
            if choice == "done":
                finished = True
            if choice in self.discoveredLocation:
                location = self.discoveredLocation[choice]
                if self.combat(location.locationHealth, location.locationAttack):
                    
                    print "You successfully invaded the %s" % location.name
                    location.spoils(game)
                    
                else:

                    print "You are not strong enough" 
    def helpout(self):

        print "Stockpile: Shows Resources"
        print "Population: Shows population status"
        print "Assign Dudes: Reassign your guys"
        print "Build: Build a building"
        print "Attack: Invade a discovered location"


    def combat(self, enemyHealth, enemyAttack):

        ourStrength = self.armyDamage * self.armyHealth
        theirStrength = enemyHealth * enemyAttack
        if ourStrength >= theirStrength:
            print "You have won"
            return True
            
        else:
            print "You have lost"
            return False
            


    def start(self):
        
        print "Welcome to the Village"
        print "There are %r people available" % self.population
        print "Let's assign some tasks"
        for professionString in self.availableProfessions:
            print "How many %ss?" % professionString
            finished = False
            while not finished:
                number = raw_input("> ")
                if False in [number[i] in '0123456789' for i in range(0, len(number))]:
                    print "That's not a number"
                else:
                    number = int(number)
                    finished = Profession(self).professionDictionary[professionString](self).add_units(self, number)
    
        self.turn_sequence()

game = Engine()
game.start()
