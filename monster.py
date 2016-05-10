"""
 Holds information and performs calculations regarding monsters, and monster skills.
   Monsters attack players, and are controlled exclusively by the AI.
 Should this become multiplayer, this logic will need to become server-side.
"""

class Monster(object):
	# variables
	x = 0	# x and y
	y = 0
	vp = 0	# vitality points

	# functions
	def __init__(self):
		print "Monster initialized."

