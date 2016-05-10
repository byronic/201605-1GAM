""" 
1GAM - a not-yet-multiplayer turn based tactical fantasy game
   (that should really be multiplayer)
 Minimum Viable Product is a single map with a single hero, and some monsters.
   Later: Terrain, additional characters, and all the proverbial spit 'n polish.

Main file. 
Functions as the entry point to the program.
 Contains the main() function, version and title information

http://www.onegameamonth.com
https://github.com/byronic

"""

__version__ = "1.0.12"

__title__ = "1GAM - May 2016"

# IMPORTS
import pygame
from pygame.locals import *
import random
from avatar import *
from monster import *

# CLASSES
# TODO: consider refactoring this into a module
class Game:
	""" 
	Added in 1.0.8
	High-level management class, authoritative
	  Manages:
	   game state; 
	   databases of monsters/avatars/maps;
	   turn execution;
	   level completion
	"""
	# game variables

	# gameState values (not final): 0 - title screen, 1 - menu, 2 - in-game
	gameState = 0
	# hold the current level index, and a list of spawned monsters that reference
	# instances of the respective database entries
	currentMap = 0
	remainingMonsters = []
	
	# databases - contain exactly what they say on the tin
	avatars = []
	monsters = []
	maps = []

	# functions
	def verbosePrint(self):
		"""
		Debugging function; prints all Game variables and databases
		TODO: Remove in release version
		"""
		print "avatars", self.avatars, "\nmonsters", self.monsters, "\nmaps", self.maps 
		print "gameState", self.gameState
		print "currentMap", self.currentMap
		print "remainingMonsters", self.remainingMonsters	

# end class Game
	
# FUNCTIONS LIBRARY

# MAIN
#   I was convinced by a neutral third-party that main()
#   is a reasonable way to organize Python
def main():
	"""
	[Non-strict] main entry point for program.
	Called explicitly at the end of file: main.py
	"""
	# Required prior to calling any pygame-related functions
	pygame.init()
	# Create the game window; set_mode((resolution), flags, depth)
	#   800x600
	window = pygame.display.set_mode((800, 600), 0, 32)
	# Title the window
	pygame.display.set_caption(__title__)

	# game state handler creation and game manager initialization
	game = Game()

	# TODO: Remove. printing verbose gamestate log as test
	game.verbosePrint()

	# Game loop
	quit = False
	while not quit:
		# handle user input
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit = True
			
	# SANDBOX - TEST AREA
	# TO BE REMOVED
	x = Avatar()
	x.getInventory()
	y = Monster()
	print y.x + y.y
	
	print "Exited cleanly."

# print version
print __title__, __version__
# writing main() is of no use if we don't call it
main()
