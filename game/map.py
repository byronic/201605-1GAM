"""
 Map class.
 Can load and save maps, keeps track of tiles for the current map
"""

colors = [(255, 255, 255), (0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 0, 0)]
"""colors contains the color for each tile type, until it becomes a sprite later in development...
so, 0 = no tile
1 = grass
2 = water
3 = lava
4 = darkness"""

class Tile:
	"""
	 Holds z-coordinate, passable data, and (if necessary) animation state for the specified tile.
	"""
	def __init__(self, x, y, graphic):
		# prepares the tile
		# serious bugfix: this function is in the form (x0/left, y0/top, width, height)
		#   but I expected/wrote the original as (x0/left, y0/top, x1/right, y1/bottom)
		#    which caused an exciting difficulty.
		self.tileDrawData = (x * 30, y * 30, 30, 30)
		self.tileGraphic = graphic
		
	z = 0
	tileGraphic = 0 # 0 - no tile, 1 - grass, 2 - water, 3 - lava
	tileDrawData = (0, 0, 0, 0)
	animationCurrentFrame = 0 # tiles can have animation frames! Important
	animationTotalFrames = 0
	passable = True # passable False: blocks movement _through_ the tile
	occupied = False # true if something is already standing here
	

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

	# TODO: Right now this function sucks/insufflates/implodes. Lose it or add more
	def generateTile(self, x, y, var):
		# placeholder -- should actually create a tile
		return Tile(x, y, var)

	def load(self, filename):
		print "Trying Map.load( " + filename + " )"
		try:
			file = open(filename)
			# schema 1.0.0 expected
			if file.readline() != "1.0.0\n":
				print "Map error: Schema not defined or inaccurate."
				return False;
			x = 0
			y = 0
			for line in file:
				if line[0] != "#": # ignore comments
					row = line.split(",")
					for var in row:
						self.tiles[str(x) + "," + str(y)] = self.generateTile(x, y, int(var))
						x = x + 1
					y = y + 1
					x = 0
			file.close()
		except:
			return False

		return True

	def save(self, filename):
		print "Map.save( " + filename + " ) was called, but the function is just a placeholder."
		return False

	def verbosePrint(self):
		"""Used in debugging."""
		print self.tiles
