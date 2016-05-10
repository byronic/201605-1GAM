class Avatar(object):
    """In-game character class. Holds character health, positions, items, and skills"""
    def __init__(self):
        print "Avatar initialized."

    def getInventory(self):
        print "Inventory."
	print self.x, self.y

    #class instance variables
    vitality = 0
    maxVitality = 0
    x = 0
    y = 0
