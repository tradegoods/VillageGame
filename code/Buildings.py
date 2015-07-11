class Building(object):


    def __init__(self, project):
        buildingList = {"House": self.MoreHousing, "Fletchery": self.Fletchery, "Forge": self.Forge, "Lumbermill": self.Lumbermill, "Blacksmith": self.Blacksmith} 
        buildingList[project]()

    def Fletchery(self):
        self.name = "Fletchery"
        self.cost = 5
    def Forge(self):
        pass

    def Lumbermill(self):
        pass

    def Blacksmith(self):
        pass

    def MoreHousing(self):
        self.name = "House"
        self.cost = 3
