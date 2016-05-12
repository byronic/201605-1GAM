"""
 Map class.
 Can load and save maps, keeps track of tiles for the current map
"""

class Tile:
	"""
	 Holds z-coordinate, passable data, and (if necessary) animation state for the specified tile.
	"""
	z = 0
	tileGraphic = 0
	animationFrame = 0
	passable = 0

class Map:
	# variables
	# The tile-types database that existed here made no sense and has been removed.
	#   Tile types without their x, y, z and sprite / animation data were generally useless.
	
	# Contains the tiles from the current map;
	#  Key-value pairs are in the form of "x,y" as in the following example:
	#  tiles["1,3"] would fetch the tile at x-coordinate 1, y-coordinate 3
	tiles = {}

	# functions
	def __init__(self):
		print "Initialized Map."

	def load(self, file):
		print "Map.load( " + file + " ) was called, but the function is just a placeholder."
		return False

	def save(self, file):
		print "Map.save( " + file + " ) was called, but the function is just a placeholder."
		return False
