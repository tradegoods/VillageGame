

class Engine(object):

    def __init__(self):
        global allBuildings 
        allBuildings = {"House": 3}
    def month_sequence(self):
        global completeProjects
        global currentProjects
        
        if len(currentProjects) == 0:
            print "You have no current projects"
        else:
            gone = []
            for project in currentProjects:
                currentProjects[project] -= 1    
                if currentProjects[project] == 0:
                    completeProjects[project] = currentProjects[project]
                else:
                    print "%s will be done in %r turns" % (project, currentProjects[project])
        print "The following projects are completed:"
        if len(completeProjects) == 0:
            print "None"
        for project in completeProjects:
            print project
            del currentProjects[project]
        completeProjects = {}    
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
                    currentProjects[choice] = allBuildings[choice]
                    print "%s will be done in %r turns" % (choice, allBuildings[choice])
        self.run_month()

    def run_month(self):
        self.month_sequence()

    def start(self):
        global completeProjects
        global availableBuildings
        global currentProjects
        

        completeProjects = {}
        currentProjects = {}
        availableBuildings = {"House": 3}
        self.month_sequence()
game = Engine()
game.start()
