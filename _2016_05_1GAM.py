""" 1GAM - a not-yet-multiplayer turn based tactical fantasy game
   (that should really be multiplayer)
 Minimum Viable Product is a single map with a single hero, and some monsters.
   Later: Terrain, additional characters, and all the proverbial spit 'n polish.

 author: Byron
"""

# IMPORTS
import pygame
import random
import sys
from avatar import *

# CLASSES

# NOT A HUGE FAN OF THE MAIN FUNCTION, so this code is all inline.
print "I'm the main game loop."

x = Avatar()
x.getInventory()

