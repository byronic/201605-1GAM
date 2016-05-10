""" 
Added in 1.0.8 as a class
Moved in 1.0.13 to module

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
def verbosePrint():
	"""
	Debugging function; prints all Game variables and databases
	TODO: Remove in release version
	"""
	print "avatars", avatars, "\nmonsters", monsters, "\nmaps", maps 
	print "gameState", gameState
	print "currentMap", currentMap
	print "remainingMonsters", remainingMonsters	
