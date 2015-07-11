from Buildings import Building

class Engine(object):

    def __init__(self):
        global allBuildings 
        allBuildings = ["House"]
    def month_sequence(self):
        global completeProjects
        global currentProjects
        
        if len(currentProjects) == 0:
            print "You have no current projects"
        else:
            for project in currentProjects:
                project.cost -= 1    
                if project.cost == 0:
                    completeProjects.append(project)
                else:
                    print "%s will be done in %r turns" % (project.name, project.cost)
        print "The following projects are completed:"
        if len(completeProjects) == 0:
            print "None"
        for project in completeProjects:
            print project.name
            #project.complete() need to change a lot
            currentProjects.remove(project)
        completeProjects = []
        print "~~~~~~~~~~"
        print "Would you like to start something else?"
        print "Available Buildings:"
        for building in availableBuildings:
            print building
        choice = " "
        while choice != "no":
            choice = raw_input("> ")
            if choice in availableBuildings:
                if choice in currentProjects:
                    print "Already Doing that Scrub"
                else:
                    project = Building(choice)
                    currentProjects.append(project)
                    print "%s will be done in %r turns" % (project.name, project.cost)
        self.run_month()

    def run_month(self):
        self.month_sequence()

    def start(self):
        global completeProjects
        global availableBuildings
        global currentProjects

        completeProjects = []
        currentProjects = []
        availableBuildings = ["House", "Fletchery"]
        self.month_sequence()
game = Engine()
game.start()
