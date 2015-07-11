from Buildings import Building

class Engine(object):

    
    
    
    def __init__(self):
        pass


    def month_sequence(self):
        if len(self.currentProjects) == 0:
            print "You have no current projects"
        else:
            for project in self.currentProjects:
                project.cost -= 1    
                if project.cost == 0:
                    self.completeProjects.append(project)
                else:
                    print "%s will be done in %r turns" % (project.name, project.cost)
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
                    print "%s will be done in %r turns" % (project.name, project.cost)
        self.run_month()

    def run_month(self):
        self.month_sequence()

    def start(self):
        self.completeProjects = []
        self.availableBuildings = ["House", "Fletchery"]
        self.currentProjects = []

        self.month_sequence()
game = Engine()
game.start()
