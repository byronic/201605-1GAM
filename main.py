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

__version__ = "1.0.17"

__title__ = "1GAM - May 2016"

# IMPORTS
import pygame
from pygame.locals import *
import random
from avatar import *
from monster import *
import game.manager

# CLASSES
# former class Game was migrated to module game.manager

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

	# Game loop
	quit = False
	while not quit:
		# draw the window
		window.fill((148, 148, 148))
		pygame.display.update()
		
		# handle user input
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit = True
	
	print "Exited cleanly."

# print version
print __title__, __version__
# writing main() is of no use if we don't call it
main()
