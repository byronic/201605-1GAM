"""
 Holds information and performs calculations regarding players, and player skills.
   Players are controlled exclusively by humans.
 Should this become multiplayer, this logic will need to become server-side.
 Additionally, a disconnected player should either:
  - change the math of monsters to re-balance
  - become AI controlled
"""

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
