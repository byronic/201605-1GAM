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

__version__ = "1.0.42"

__title__ = "1GAM - May 2016"

# IMPORTS
import pygame
from pygame.locals import *
import random
from game.avatar import *
from game.monster import *
from game.map import *
import game.manager

# CLASSES
# former class Game was migrated to module game.manager

# FUNCTIONS LIBRARY

def drawAvatars(window):
	for av in game.manager.avatars:
		# for now, no sprites, so drawing a black rectangle for avatars
		pygame.draw.rect(window, colors[4], (av.x * 30 + 5, av.y * 30 + 5, 20, 20))

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

	# Create and initialize test map
	level = Map()
	level.load("assets/test.map")

	# debugging
	print level.tiles["25,15"].tileGraphic
	game.manager.avatars.append(Avatar())



	# Game loop
	quit = False
	while not quit:
		# draw the window
		# TODO: This entire draw function needs serious optimization
		#         such as updating part of the screen only when necessary at a capped max fps
		window.fill((148, 148, 148))
		
		# draw the tileset in order
		for key in level.tiles:
			if level.tiles[key].tileGraphic != 0:
				pygame.draw.rect(window, colors[level.tiles[key].tileGraphic], level.tiles[key].tileDrawData)

		# draw all avatars
		drawAvatars(window)

		# presents the frame update to the user - without this we 'draw' in memory
		#  but nothing would ever be displayed
		pygame.display.update()
		
		# handle user input
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				game.manager.clickedTile = pygame.mouse.get_pos()
				game.manager.clickedTile = (game.manager.clickedTile[0] / 30,
								game.manager.clickedTile[1] / 30)
				print game.manager.clickedTile
			elif event.type == QUIT:
				pygame.quit()
				quit = True
	
	print "Exited cleanly."

# print version
print __title__, __version__
# writing main() is of no use if we don't call it
main()
