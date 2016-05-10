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

	# variables
	# player health does not have a maximum
	health = 6
	# player position as (x, y, z) coordinates
	x = 0
	y = 0
	z = 0

	# functions
	def __init__(self):
		print "Avatar initialized."

	def verbosePrint(self):
		"""
		Prints current class data to console, in its entirety.
		For debugging use.
		"""
		print "health", self.health
		print "(x, y, z) = (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

