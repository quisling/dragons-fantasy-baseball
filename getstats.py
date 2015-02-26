from stats import *

def get_stats(game, player, player_type):
	"""From a Game Number, a Player Name, and type, returns statblock
	"""
	if player_type == "Position Player":
		return get_hitter_stats(game, player)
	elif ((player_type == "Starting Pitcher") or
		 (player_type == "Relief Pitcher")):
		return get_pitcher_stats(game, player)
	else:
		raise NotImplementedError("No Such Player Type")

def get_hitter_stats(game, player):
	"""From a Game Number, a Player Name, returns hitter statblock
	
	This presently returns test data, of 1 of each value
	"""
	return HitStatBlock(1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
						1, 1, 1, 1)

def get_pitcher_stats(game, player):
	"""From a Game Number, a Player Name, returns pitcher statblock
	
	This presently returns test data, of 1 of each value
	"""
	return PitchStatBlock(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
						  1, 1, 1, 1, 1, 1, 1)

def get_empty_stats(player_type):
	if player_type == "Position Player":
		return HitStatBlock()
	elif ((player_type == "Starting Pitcher") or
		 (player_type == "Relief Pitcher")):
		return PitchStatBlock()
	else:
		raise NotImplementedError("No Such Player Type")
