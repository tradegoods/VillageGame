from Buildings import Building
from Professions import Profession
class Engine(object):
        
    
    
    def __init__(self):
        self.productivity = 0
        self.population = 8
        self.freePopulation = 8
        self.completeProjects = []
        self.availableBuildings = ["House", "Fletchery"]
        self.currentProjects = []
        self.availableProfessions = ["Builder", "Farmer", "Scout"]
        self.professionAssigned = {}
        self.commandDictionary = {"Stockpile": self.stockpile, "Population": self.population_status, "Available Buildings": self.available_buildings, "Assign Dudes": self.assign_dudes}
        self.resources = {"Wood": 0, "Food": 10}
        self.foodPerTurn = -8
        self.woodPerTurn = 0
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
            self.random_event()

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
            project.cost -= self.productivity    
            if project.cost <= 0:
                self.completeProjects.append(project)
            for project in self.completeProjects:
                project.complete(self)
                self.currentProjects.remove(project)
        self.completeProjects = []

    def random_event(self):
        pass
    
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
        while choice != "no":
            choice = raw_input("> ")
            if choice in self.availableBuildings:
                if choice in self.currentProjects:
                    print "Already Doing that Scrub"
                else:
                    project = Building().buildingList[choice]()
                    self.currentProjects.append(project)
                    print "%s will be done in %r turns" % (project.name, (project.cost / self.productivity + (project.cost % self.productivity != 0)))
        	

    def assign_dudes(self):

	print("Reassign Dudes?")
        choice = " "
        while not "no" in choice:
            choice = raw_input("> ").split(" ")
            if choice[0] in self.availableProfessions:
                number = int(choice[1])
                self.professionAssigned[choice[0]].add_units(self, number)    

 
    def start(self):
        
        print "Welcome to the Village"
        print "There are %r people available" % self.population
        print "Let's assign some tasks"
        for professionString in self.availableProfessions:
            print "How many %ss?" % professionString
            number = int(raw_input("> "))
            Profession(self).professionDictionary[professionString](self).add_units(self, number)
    
        self.turn_sequence()

game = Engine()
game.start()
