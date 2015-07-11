from Buildings import Building
from Professions import Profession
class Engine(object):

    
    
    
    def __init__(self):
        pass
        self.productivity = 0
        self.population = 8
        self.freePopulation = 8
        self.completeProjects = []
        self.availableBuildings = ["House", "Fletchery"]
        self.currentProjects = []
        self.availableProfessions = ["Builder", "Farmer"]


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
        self.month_sequence()

    def start(self):
        
        print "Welcome to the Village"
        print "There are %r people available" % self.population
        print "Let's assign some tasks"
        for professionString in self.availableProfessions:
            print "How many %ss?" % professionString
            number = int(raw_input("> "))
            profession = Profession().professionDictionary[professionString]().add_units(self, number)
        self.month_sequence()

game = Engine()
game.start()
