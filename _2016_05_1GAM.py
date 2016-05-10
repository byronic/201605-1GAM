""" 
1GAM - a not-yet-multiplayer turn based tactical fantasy game
   (that should really be multiplayer)
 Minimum Viable Product is a single map with a single hero, and some monsters.
   Later: Terrain, additional characters, and all the proverbial spit 'n polish.

 author: Byron

http://www.onegameamonth.com
https://github.com/byronic

"""

__version__ = "1.0.4"

# IMPORTS
import pygame
from pygame.locals import *
import random
import sys
from avatar import *
from monster import *

# CLASSES

# FUNCTIONS

# MAIN
#   I was convinced by a neutral third-party that main()
#   is a reasonable way to organize Python
def main():
	"""
	[Non-strict] main entry point for program.
	Called explicitly at the end of file: main.py
	"""

	# SANDBOX - TEST AREA
	# TO BE REMOVED
	x = Avatar()
	x.getInventory()
	y = Monster()
	print y.x + y.y

# print version

# writing main() is of no use if we don't call it
main()
